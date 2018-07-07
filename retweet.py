# Retweet bot for Twitter, using Python and Tweepy.
# Search query via hashtag or keyword.
# Author: Vinod Nimbalkar
# Date: Saturday, July 7th - 2018.

import tweepy
from time import sleep
# Import in your Twitter application keys, tokens, and secrets.
# Make sure your credentials.py file lives in the same directory as this .py file.
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Where q='#example', change #example to whatever hashtag or keyword you want to search.
# Where items(5), change 5 to the amount of retweets you want to tweet.
# Make sure you read Twitter's rules on automation - don't spam!
for tweet in tweepy.Cursor(api.search, q='#वारी').items(5):
    try:
        tweet.retweet()
        print('Retweet published successfully.')

        # Where sleep(60*30), sleep is measured in seconds.
        # Change 60*30 to amount of seconds you want to have in-between retweets.
	# Here 60*30 means 1800 second i.e 30 minute.
        # Read Twitter's rules on automation. Don't spam!
        sleep(60*30)

    # Some basic error handling. Will print out why retweet failed, into your terminal.
    except tweepy.TweepError as error:
        print('\nError. Retweet not successful. Reason: ')
        print(error.reason)

    except StopIteration:
        break
