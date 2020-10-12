import tweepy
from textblob import TextBlob
import json

def setup():
    with open("keys.json") as f:
        stuff = json.load(f)
    auth = tweepy.OAuthHandler(stuff["key"], stuff["secret"])
    auth.set_access_token(stuff["access token"], stuff["access token secret"])
    return tweepy.API(auth)

