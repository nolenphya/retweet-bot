# Retweet bot for Twitter, using Python and Tweepy. 

# This bot will automatically grab tweets, perform sentiment analysis,
# and then retweet depending on the given parameters below. 

# I eventually want to make this more complex so that the user 
# will be able to type in whehter they want to retweet based on positive or negative sentiment.

# Search query via hashtag or keyword.
# Author: Nolen Phya
# Date: November, 18
## NOTES: I adapted some of this code from Tyler L. Jones

from textblob import TextBlob
import tweepy
import seaborn as sns
import pandas
from time import sleep


# Import in your Twitter application keys, tokens, and secrets.
# Make sure your keys.py file lives in the same directory as this .py file.

from keys import *

CONSUMER_KEY = 'consumer key'
CONSUMER_SECRET = 'consumer secret'
ACCESS_KEY = 'access key'
ACCESS_SECRET = 'access secret'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

print('Hello! I am retweet bot. I will retweet tweets based on the search term you define for me.')
print('SEARCH TERM:')
keyword_input = input()
print('\n')
print('Please define how many tweets you would like to analyze at once. \nBe careful of spamming and remember to always follow the rules!')
item_input = input()
input_int = int(item_input)

for tweet in tweepy.Cursor(api.search, q=keyword_input).items(input_int):
    try:
        print('\nRetweet bot found tweet. Analyzing now:' + tweet.text)
        analysis = TextBlob(tweet.text)
        print(analysis.sentiment)
        if analysis.sentiment.polarity > 0:
            print('\nAttempting to retweet now...')
            api.retweet(tweet.id)
            print('\nRetweet published successfully. Moving to next tweet.')
        # Where sleep(10), sleep is measured in seconds.
        # Change 10 to amount of seconds you want to have in-between retweets.
        # Read Twitter's rules on automation. Don't spam!
            sleep(60*3)

    # Some basic error handling. Will print out why retweet failed, into your terminal.
    except tweepy.TweepError as error:
        print('\nError. Retweet not successful. Reason: ')
        print(error.reason)

    except StopIteration:
        break
