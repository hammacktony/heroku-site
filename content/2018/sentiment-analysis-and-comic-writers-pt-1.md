---
date: 2018-10-30
title: Sentiment Analysis and Comic Writers pt. 1
cover: https://th-website.s3-website.us-east-2.amazonaws.com/blog/img/twitter_upload.png
categories:
    - Tech
tags:

    - Sentiment Analysis

---

## Introduction

As a staff writer for [thebatmanuniverse.net](thebatmanuniverse.net), I am a member of our Discord server. Discord is a place where we, as the staff, interact our community. Often, there are debates about stories, writers, and artists. Currently at DC, there is a polarizing writer who writes the current arc of Detective Comics. Needless to say, those on the server do not like his writing, especially me. 

I asked myself if other people felt the same way. When in doubt, check Twitter. My goal is to search tweets that mention different comics writers and determine if people like or dislike them. This is a classic sentiment analysis problem. 

I will be releasing more posts as progress continues on this project. For now, here is how I connected to the Twitter API and uploaded the tweets to MongoDB for further analysis. The following code can be seen at [Github](https://github.com/hammacktony/comics_sentiment_analysis).

## Connecting to Twitter

In the Python ecosystem, there are several packages that can access the Twitter API. I am using [Tweepy](http://www.tweepy.org/). For the authentication handler, I am using the `tweepy.AppAuthHandler`. I am using this class because it allows the application to exceed the max download limit of tweets. To set up the api instance, I used the following function.

```
def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with our access keys provided.

    returns
        tweepy.Api instance

    """

    # Authentication and access using keys:
    auth = tweepy.AppAuthHandler(
        twitter_credentials.CONSUMER_KEY,
        twitter_credentials.CONSUMER_SECRET
    )
    auth.secure = True
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    return api
```

## MongoDB

To store tweets for sentiment analysis, I decided to use a MongoDB backend. I decided on MongoDB because the json api responses would easily be stored in the document-based format of MongoDB. This structure is what separates MongoDB from relational databases. 

To connect with my MongoDB database, I used the Python library [Pymongo](https://api.mongodb.com/python/current/). It is the recommended way to work with MongoDB with Python. 

In `settings.py`, I initialized the connection by

```
''' Getting credentials and initializing connections '''
import os
from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient

load_dotenv(find_dotenv())

...

# MongoDB Connection
client = MongoClient(os.getenv('MONGODB_URI'))
mongo = client.heroku_v6ds7xrr
```

As I set up a few collections just for development. The comic creators I want to study are DC Comics' Tom King, Scott Snyder, James Tynion IV, Joëlle Jones, Geoff Johns, and James Robinson. I created their collections via:

```
mongo_connections = {
    'Tom King': mongo.t_king,
    'Scott Snyder': mongo.s_snyder,
    'James Tynion': mongo.j_t4,
    'Joelle Jones': mongo.j_jones,
    'Geoff Johns': mongo.g_johns,
    'James Robinson': mongo.j_robinson,
}
```

## Upload


To save space, I extracted the text from the api response, and then cleaned the tweet by removing links and special characters. 

```
''' Helper functions for upload.py '''
import re

from typing import Dict


def clean_text(text: str) -> str:
    '''
    Utility function to clean text by removing
    links and special characters using regex.

    args
        text: str - text that needs to be cleaned

    return
        str - Cleaned text
    '''

    return ' '.join(
        re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)",
               " ", text).split())



def get_tweet(tweet_json: Dict[str, str]) -> str:
    '''
    Get tweet from Twitter Api Resonse

    args
        tweet_json: dict - Twitter Api Response

    return
        str - text of tweet
    '''

    tweet_text = tweet_json['text']
    return clean_text(tweet_text)

```

After initializing the MongoDB collections,
I created the following function to retrieve tweets. This function is heavily inspired by this StackOverflow [answer](https://stackoverflow.com/questions/38555191/get-all-twitter-mentions-using-tweepy-for-users-with-millions-of-followers).

```
def upload_tweets(api, searchQuery: str, ) -> None:
    ''' Connects uploads the tweets to mongodb give query

    args
        str - searchQuery: search parameter    
    '''

    # Initialize
    retweet_filter: str = '-filter:retweets'
    q = searchQuery+retweet_filter
    tweetsPerQry: int = 100
    tweetCount: int = 0
    max_id = -1
    maxTweets: int = 5000
    sinceId = None
    conn = mongo_connections[searchQuery]

    while tweetCount < maxTweets:
        try:
            if max_id <= 0:
                if not sinceId:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry)
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            since_id=sinceId)
            else:
                if not sinceId:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            max_id=str(max_id - 1))
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                            max_id=str(max_id - 1),
                                            since_id=sinceId)
            if not new_tweets:
                print("No more tweets found")
                break
            for tweet in new_tweets:
                # Upload to MongoDB collection
                conn.insert_one({'text': get_tweet(tweet._json)})
            tweetCount += len(new_tweets)
            print(f"Downloaded {tweetCount} tweets")
            max_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            # Just exit if any error
            print("some error : " + str(e))
            break
``` 

The important variables in this function are `tweetsPerQry` and `maxTweets`. These variables determine how many tweets can be queried at one time and the maximum number of tweets you want to download in general.

## Upload tweets

The creators' Twitter handles are stored in `queries.py`. Iterating through these handles in conjunction with `upload_tweets()`, we are able to upload the tweets of each creator to their corresponding MongoDB collection.

```
api = twitter_setup()

print('Beginning Upload')
for searchQuery in queries:
    print('Tweets for @'+f'{searchQuery}')
    upload_tweets(api, searchQuery)
print('Upload Complete')
```

## Conclusion

I have detailed how to access the Twitter API and upload tweets to MongoDB collections. As I continue this project, I will write updates on my progress. Part 2 in this series will deal with how I collected Reddit posts to supplement Twitter data for sentiment analysis.

You can follow my progress on [Github](https://github.com/hammacktony/comics_sentiment_analysis).

Stay Tuned!