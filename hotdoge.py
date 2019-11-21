import tweepy
import keyboard
import time
import random

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']

while True:
    try:
        random_letters = random.choice(letters) + random.choice(letters) + random.choice(letters) + random.choice(
            letters) + random.choice(letters)
        tweet = random_letters
        api.update_with_media('hotdoge.png', status=tweet)
        time.sleep(3600)
