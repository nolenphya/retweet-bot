# Retweet bot for Twitter, using Python and Tweepy. 

# This bot will automatically grab tweets, perform sentiment analysis,
# and then retweet depending on the given sentiment paramters. 

# I eventually want to make this more complex so that the user 
# will be able to type in their keywords and retweet parameters. 

# Search query via hashtag or keyword.
# Author: Nolen Phya
# Date: November, 17
# NOTES: I adapted some of this code from Tyler L. Jones

# Make sure you download all these packages first!

from textblob import TextBlob
import tweepy
import seaborn as sns
import pandas
from time import sleep

# Put your own keys here!

CONSUMER_KEY = 'consumer key'
CONSUMER_SECRET = 'consumer secret'
ACCESS_KEY = 'access key'
ACCESS_SECRET = 'access secret'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# Where q='#example', change #example to whatever hashtag or keyword you want to search.
# NOTE: instead of && or || operators, you use AND and OR
# Where items(5), change 5 to the amount of retweets you want to tweet.
# Make sure you read Twitter's rules on automation - don't spam!

for tweet in tweepy.Cursor(api.search, q='green new deal OR #greennewdeal').items(5):
    try:
        print('\nRetweet bot found tweet. Analyzing now:' + tweet.text)
        analysis = TextBlob(tweet.text)
        print(analysis.sentiment)
        if analysis.sentiment.polarity > 0:
            print('\nAttempting to retweet now...')
            api.retweet(tweet.id)
            print('Retweet published successfully.')
        # Where sleep(10), sleep is measured in seconds.
        # Change (10) change to amount of seconds, minutes or hours you want to have in-between retweets.
        # Read Twitter's rules on automation. Don't spam!
            sleep(10)

    # Some basic error handling. Will print out why retweet failed, into your terminal.
    except tweepy.TweepError as error:
        print('\nError. Retweet not successful. Reason: ')
        print(error.reason)

    except StopIteration:
        break
