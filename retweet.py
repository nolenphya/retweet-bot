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
