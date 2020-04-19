---
date: 2018-11-01
title: Sentiment Analysis and Comic Writers pt. 3
cover: ./images/calculate_stats.webp
categories:
    - Tech
tags:

    - Sentiment Analysis

---

## Introduction

In previous posts, I detailed my quest to gather data to analyze how the public viewed certain comics creators. The two best ways to poll the internet these days are searching Twitter and Reddit. Thankfully, each have APIs I can access.

Today, I am discussing how I used this data to create sentiment scores for each post and gathered important statistics for future analysis.

## Detailing the Problem

When I initially started this project, I believed this would be a good introductory project where I would learn important skills for the future. I did not realize how undefined my problem was.

Using [Textblob](https://textblob.readthedocs.io/en/dev/) for sentiment analysis, there exists three classifications a post can have: positive, neutral, and negative sentiments. 

How do you quantify success then? One could study the mean of all tweets with positive, neutral, and negative sentiments, and sort the means of the negatives and positives. But, this is not a true picture of the sentiments of the population.

One could also calculate the mean of all scores to create a single score to measure popularity. Once again this will be skewed. 

There are a few reasons the above will not work:

1. They fail to account for historical patterns.
2. They fail to account for small population sizes.
3. They fail to predict the actual sentiment scores.
4. They offer incorrect sorting techniques.

The best way to circumvent the deficiencies of points 1-3 is finding the mean of the posterior distribution of each of the three sentiment scores. The way to determine this posterior distribution is by [Markov chain Monte Carlo](https://en.wikipedia.org/wiki/Markov_chain_Monte_Carlo). We can look at the mean and standard deviation of this posterior distribution to determine the "true" sentiment scores within a certain amount of certainty. 

The best way to sort these scores is using the lower bound of [Wilson score confidence interval](https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval#Wilson_score_interval) for a Bernoulli parameter. Essentially, this ranks which distributions are the best by comparing the worst possible case. This provides a "truer" sense of how these distributions are ranked. 

The rest of this post will detail how I collected the necessary statistics for the above analysis and stored them for future use.

## Collecting Sentiment Scores

For MCMC, I need a lot of data to generate an accurate prior. To gather this information on these sentiment scores, I used [Textblob](https://textblob.readthedocs.io/en/dev/). Textblob allows for "easy" natural language processing. Eventually, I want to create my own machine learning model, but there is not a corpus of comics tweets to analyze, yet. 

_(I am creating that now actually.)_ 

To create a `Textblob` instance, I need to initiate the class with the text I want to analyze. When I initiate this object, I have access to multiple attributes and methods. The main attribute I am interested in is the object's sentiment score. This is returned to the user as a `NamedTuple`. From there, we can choose the `polarity` attribute. This will give us either positive or negative sentiment scores, with 0 representing neutral sentiment. To calculate the sentiment scores, I used a scale consisting of 1, 0, and -1 for positive, neutral, and negative scores respectively.

```

""" Helper function for sentiment analysis """

from textblob import TextBlob
from queries import queries


def analyze_sentiment(post: str) -> int:
    """
    Utility function to classify the polarity of a post
    using textblob.

    args
        str - Text of post

    returns
        int - sentiment analysis score (scale from 1-3)
    """

    analysis = TextBlob(post)
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1
        
```

## Calculating the Statistics

This is the simple part, the main "statistical" calculations I did were calculating the mean and standard deviation of sentiment scores per writer. Here is the function that calculates the statistics.

```
...

def app(handle: str) -> Tuple:
    """ Connect to mongodb to get posts about a creator
    and declare those posts are positive, neutral, or negative
	
    args
        str - handle: Name creator in mind
	
    returns
         tuple - Returns name, 
                    len of posts about person, 
                    mean of postive posts,
                    standard deviation of postive posts, 
                    mean of neutral posts, 
                    standard deviation of neutral posts, 
                    mean of negative posts,
                    standard deviation of negative posts 
    """
	
    # Initialize
    conn = mongo_connections[handle]
    posts = [doc['text'] for doc in conn.find()]
	
    # We create a list with the result of the analysis:
    sentiment_scores = list(map(analyze_sentiment, posts))
	
    # Each type of post
    pos_posts, neu_posts, neg_posts = list(), list(), list()
	
    # Collect sentiments for each type of post
    for i in range(len(sentiment_scores)):
        # Basic idea is one-hot encoding data at each index i
        if sentiment_scores[i] == 1:
            pos_posts.append(1)
            neu_posts.append(0)
            neg_posts.append(0)
        if sentiment_scores[i] == 0:
            pos_posts.append(0)
            neu_posts.append(1)
            neg_posts.append(0)
        if sentiment_scores[i] == -1:
            pos_posts.append(0)
            neu_posts.append(0)
            neg_posts.append(1)
	
    try:
        # Calculate mean and std of posts
        pos_mean, pos_std = np.mean(pos_posts), np.std(pos_posts)
        neu_mean, neu_std = np.mean(neu_posts), np.std(neu_posts)
        neg_mean, neg_std = np.mean(neg_posts), np.std(neg_posts)
	
    ...
	
    data = (handle, len(posts), pos_mean, pos_std,
            neu_mean, neu_std, neg_mean, neg_std)
    return data
```
    
Now, everything is obvious except the `for` and `if` statements. I have to pad the other arrays when one of the computed sentiment scores is either -1, 0, or 1. If not, then I will collect an array that contains either all -1's, 0's, or 1's. These arrays will have means of -1, 0, -1 and a standard deviations of 0 respectively.

This obviously is a problem.

 _(This technique is akin to one-hot encoding categorical variables in a dataset.)_

After computing these statistics, I uploaded them to MongoDB in special collections. These collections are defined in `settings.py` as: 

```
...

# Upload stats on each writer
mongo_connections_stats = {
    'Tom King': mongo.t_king_stats,
    'Scott Snyder': mongo.s_snyder_stats,
    'James Tynion': mongo.j_t4_stats,
    'Joelle Jones': mongo.j_jones_stats,
    'Geoff Johns': mongo.g_johns_stats,
    'James Robinson': mongo.j_robinson_stats,
}
```


To upload these stats to MongoDB:

```
def upload_stats(query: str, test: bool = False) -> Dict[str, str]:
    ''' Upload stats to MongoDB

    args
        str (query) - name you want to query
        bool (test) - If in test mode, it does not submit 
            new stats data to MongoDB
    '''
    # Retrieve current time
    now = datetime.datetime.now()
    current = now.strftime("%Y-%m-%d %H: %M")

    # Begin upload of statistics
    print(f'Begin Upload of {query} stats')
    data = app(query)

    result = {
        'time': current,
        'creator': data[0],
        'total tweets': data[1],
        'postive_mean': data[2],
        'postive_std': data[3],
        'neutral_mean': data[4],
        'neutral_std': data[5],
        'negative_mean': data[6],
        'negative_std': data[7],
    }

    # Upload stats
    print(f'Upload stats for {query}')

    if test == True:
        # Bypasses uploaded data to MongoDB
        return result

    conn = mongo_connections_stats[query]
    conn.insert_one(result)
    
    print('End Upload')
```

The test parameter is just so when I use `pytest` to make sure I did not break my application, I have not uploaded new stats. In test mode, it just calculates the statistics (returned as a dictionary object).

_(This is what would be uploaded to MongoDB. There is another test to make sure our_ `pymongo` _connection is initiated.)_

## Conclusion

I hope it is obvious the hardest part about this entire project is **defining the problem and necessary steps to collect data**.

These stats are calculated and uploaded to MongoDB each hour. (Thanks Heroku Scheduler plugin!) I will let this calculate and collect data for a few weeks.

Next post will be about how I used `pymc` to calculate my prior and posterior distributions of the statistics of positive, neutral, and negative posts.

If you want to follow my work, my Github repository can be found [here](https://github.com/hammacktony/comics_sentiment_analysis).

---

Be sure to checkout the rest of my blog! I am constantly writing about cool stuff I am working on and have learned recently!