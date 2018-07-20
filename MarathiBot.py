# Retweet bot for Twitter, using Python and Tweepy.
# Search query via hashtag or keyword.
# Author: Vinod Nimbalkar
# Date: Saturday, July 7th - 2018.

import tweepy
from time import sleep
import time
import schedule
# Import in your Twitter application keys, tokens, and secrets.
# Make sure your credentials.py file lives in the same directory as this .py file.
from credentials import *
import data

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def retweet():
    # Where q='#example', change #example to whatever hashtag or keyword you want to search.
    # Where items(5), change 5 to the amount of retweets you want to tweet.
    # Make sure you read Twitter's rules on automation - don't spam!
    for tweet in tweepy.Cursor(api.search, q='#वारी OR #पाऊस').items(5):
        try:
            tweet.retweet()
            print('Tweet by: @' + tweet.user.screen_name)
            print('Retweet published successfully.')

            if not tweet.user.following:
                tweet.user.follow()
                print('Followed the user' + tweet.user.screen_name)

        # Some basic error handling. Will print out why retweet failed, into your terminal.
        except tweepy.TweepError as error:
            print('\nError. Retweet not successful. Reason: ')
            print(error.reason)

        except StopIteration:
            break

def favorite():
    # Where q='#example', change #example to whatever hashtag or keyword you want to search.
    # Where items(5), change 5 to the amount of favorites you want to tweet.
    # Make sure you read Twitter's rules on automation - don't spam!
    for tweet in tweepy.Cursor(api.search, q='#वारी').items(5):
        try:
            tweet.favorite()
            print('Tweet Favorited successfully.')

        # Some basic error handling. Will print out why favorite failed, into your terminal.
        except tweepy.TweepError as error:
            print('\nError. Favorite not successful. Reason: ')
            print(error.reason)

        except StopIteration:
            break
            
def batami():
    news = data.marathiNews()
    message = "ताजी बातमी : "
    message += news
    try:
        api.update_status(message)
        print('News Posted successfully.')

    except tweepy.TweepError as error:
            print('\nError. News posted failed. Reason: ')
            print(error.reason)
    
def aajachaSuvichar():
    quote = data.suvichar()
    message = "सुविचार : "
    message += quote
    try:
        api.update_status(message)
        print('Quote posted successfully.')
    except tweepy.TweepError as error:
        print('\n Quote posted failed because : ')
        print(error.reason)

def aajVishesh():
    vishesh = data.dinVishesh()
    message = "दिनविशेष : "
    message += vishesh
    try:
        api.update_status(message)
        print('DinVishesh Posted successfully.')

    except tweepy.TweepError as error:
            print('\nError. DinVishesh posted failed. Reason: ')
            print(error.reason)

if __name__ == "__main__":
    schedule.every(30).minutes.do(retweet)
    schedule.every(2).hours.do(batami)
    schedule.every().day.at("07:30").do(aajachaSuvichar)
    schedule.every().day.at("06:30").do(aajVishesh)
    while True:
        schedule.run_pending()
        time.sleep(1)