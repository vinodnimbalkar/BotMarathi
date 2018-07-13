# Retweet bot for Twitter, using Python and Tweepy.
# Search query via hashtag or keyword.
# Author: Vinod Nimbalkar
# Date: Saturday, July 7th - 2018.

import tweepy
from time import sleep
from threading import Thread
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
    for tweet in tweepy.Cursor(api.search, q='#वारी').items(5):
        try:
            tweet.retweet()
            print('Tweet by: @' + tweet.user.screen_name)
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

def favorite():
    # Where q='#example', change #example to whatever hashtag or keyword you want to search.
    # Where items(5), change 5 to the amount of favorites you want to tweet.
    # Make sure you read Twitter's rules on automation - don't spam!
    for tweet in tweepy.Cursor(api.search, q='#वारी').items(5):
        try:
            tweet.favorite()
            print('Tweet Favorited successfully.')

            # Where sleep(60*30), sleep is measured in seconds.
            # Change 60*30 to amount of seconds you want to have in-between favorites.
            # Here 60*30 means 1800 second i.e 30 minute.
            # Read Twitter's rules on automation. Don't spam!
            sleep(60*30)

        # Some basic error handling. Will print out why favorite failed, into your terminal.
        except tweepy.TweepError as error:
            print('\nError. Favorite not successful. Reason: ')
            print(error.reason)

        except StopIteration:
            break
            
def batami():
    quote = data.marathiNews()
    message = "ताजी बातमी : "
    message += quote
    try:
        api.update_status(message)
        print('News Posted successfully.')
        #Sleep for two hour
        sleep(60*120)
    except tweepy.TweepError as error:
            print('\nError. News posted failed. Reason: ')
            print(error.reason)
    
def aajachaSuvichar():
    pass

def aajVishesh():
    vishesh = data.dinVishesh()
    message = "दिनविशेष : "
    message += vishesh
    try:
        api.update_status(message)
        print('DinVishesh Posted successfully.')
        #Sleep for one day
        sleep(60*60*24)
    except tweepy.TweepError as error:
            print('\nError. DinVishesh posted failed. Reason: ')
            print(error.reason)

if __name__ == "__main__":
    retweet_thread = Thread(target=retweet)
    #favorite_thread = Thread(target=favorite)
    batami_thread = Thread(target=batami)
    aajachaSuvichar_thread = Thread(target=aajachaSuvichar)
    aajVishesh_thread = Thread(target=aajVishesh)

    #Will execute each thread in parallel
    retweet_thread.start()
    #favorite_thread.start()
    batami_thread.start()
    aajachaSuvichar_thread.start()
    aajVishesh_thread.start()

    #This waits until the thread has completed
    retweet_thread.join()
    #favorite_thread.join()
    batami_thread.join()
    aajachaSuvichar_thread.join()
    aajVishesh_thread.join()