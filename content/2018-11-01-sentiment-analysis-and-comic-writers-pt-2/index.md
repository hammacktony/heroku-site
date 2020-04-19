---
date: 2018-11-01
title: Sentiment Analysis and Comic Writers pt. 2
author: Tony Hammack
cover: ./images/reddit.webp
categories:
    - Tech
tags:

    - Sentiment Analysis

---

## Introduction

In [part 1](http://www.tonyhammack.com/blog/post/sentiment-analysis-and-comic-writers-pt-1), I used `tweepy` and the Twitter api to download tweets of certain comics creators. I realized comics readers use other mediums to disclose their displeasure. Reddit and 4chan are popular avenues outside Twitter were people state their opinions and criticisms of comics writers. In this post, I will detail how I retrieved posts pertaining from Reddit pertaining to certain writers and upload them to MongoDB.

## The Reddit API

Thankfully, the Reddit api has all the functionality I need. I can use the same methodology as downloading tweets from the Twitter api.

Python has a package called [praw](https://praw.readthedocs.io/en/latest/), which stands for Python Reddit API Wrapper. This package is the main way programmers - using Python - can communicate with the api. 

To connect to the Reddit api, I need to do some setup work first. Instead of recreating the wheel, here is the [link](http://www.storybench.org/how-to-scrape-reddit-with-python/) I used to gather what credentials I needed from Reddit. 

In my `settings.py` file, I loaded my Reddit credentials from my `.env` to connect to the api.

```
...

# Establishing Reddit Credentials
REDDIT = namedtuple(
    'REDDIT', 'CLIENT_ID CLIENT_SECRET USER_AGENT USERNAME PASSWORD')

reddit_credentials = REDDIT(os.getenv('REDDIT_CLIENT_ID'),
                            os.getenv('REDDIT_CLIENT_SECRET'),
                            os.getenv('REDDIT_USER_AGENT'),
                            os.getenv('REDDIT_USERNAME'),
                            os.getenv('REDDIT_PASSWORD'))
```

In `uploaders/reddit.py`, I created a function `reddit_setup()` to initiate the Reddit api connection.

```
def reddit_setup():
    ''' Create reddit instance 

    returns
        api: Reddit - Reddit instance'''

    api = Reddit(client_id=reddit_credentials.CLIENT_ID,
                         client_secret=reddit_credentials.CLIENT_SECRET,
                         user_agent=reddit_credentials.USER_AGENT,
                         username=reddit_credentials.USERNAME,
                         password=reddit_credentials.PASSWORD)
    return api
```

## Get Posts

If you are unfamiliar with Reddit, Reddit content is sub-divided by subreddits. Subreddits are the main threads where content is talked about. My plan is to search particular subreddits for mentions of the creators in question. 

These posts in subreddits are sorted by various criteria. They are sorted if they are the top talked about, if their popularity is rising, if they are new, if there is a sudden talk about them, and if they are controversial. These criteria are methods of the `Reddit` class. 

To actually gather the posts, I need to search within the subreddit (given the criteria. This is done by the following function. (I will only show one of the functions because the other four differ by the sorting criterion.)

```
def criteria_rising(conn, r_subreddit, query: str, limit: int) -> None:
    ''' Search the 'Rising' criteria for rising posts 
    
    args
        conn: MongoDB collection - collection for comic creator
        r_subreddit: Reddit subreddit instance - current subreddit
        limit: int - limit for posts to download, defaults for 1000 posts
    '''

    subreddit_in_question = r_subreddit.rising(limit=limit)

    for submission in subreddit_in_question:
    	 # Clean text by removing links and special characters
        post = clean_text(submission.selftext)
        if query in post:
            conn.insert_one({'text': post})
```

The full function which uploads posts is the following.

```
def upload_posts(api, subreddits, query: str, limit: int = 1000) -> None:
    ''' Upload posts to MongoDB 

    args
        api: praw.Reddit - Reddit instance
        subreddits: list - subreddits I want to search
        query: str - query parameter
        limit: int - limit for posts to download, defaults for 1000 posts
    '''

    conn = mongo_connections[query]

    for subreddit in subreddits:
        print(f'Searching {subreddit} for posts\n')
        r_subreddit = api.subreddit(subreddit)

        # Get posts according to topics
        print('Searching Top')
        criteria_top(conn, r_subreddit, query, limit)
        print('Searching Rising')
        criteria_rising(conn, r_subreddit, query, limit)
        print('Searching New')
        criteria_new(conn, r_subreddit, query, limit)
        print('Searching Hot')
        criteria_hot(conn, r_subreddit, query, limit)
        print('Searching Controversial')
        criteria_controversial(conn, r_subreddit, query, limit)
```

There are specifically two subreddits I want to search. They are `subreddits = ['comicbooks', 'DCcomics']`, hence the loop.

## Putting It All Together

Here is the complete function that searches per comic creator and subreddit in question and uploads posts to MongoDB.

```
def reddit():
    api = reddit_setup()

    subreddits = ['comicbooks', 'DCcomics']
    limit = 10**5

    # Upload tweets
    print('Beginning Upload')
    for query in queries:
        print(f'\nPosts for {query}')
        upload_posts(api, subreddits, query, limit)
        
    print('Upload Complete')
```

Note: Yes, I realize having a limit of 10^5 would seem to unreasonable. However in testing, the most posts I found containing a creator where 57. Thus, the large limit is needed to gather information. Feel free to play with this number.

## Conclusion

Using the Reddit API to search multiple subreddits for comics creators is not hard. It is surprisingly easier than I thought it would be.

These Reddit posts will supplement the Twitter data in our MongoDB database.

Stay tuned for part 3 where I discuss how I created the sentiment scores.

You can follow my progress on [Github](https://github.com/hammacktony/comics_sentiment_analysis).