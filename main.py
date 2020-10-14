import tweepy
from textblob import TextBlob
import json
from collections import deque

users = deque(maxlen=100)
rawds = deque(maxlen=100)
datas = deque()

def setup():
    with open("keys.json") as f:
        stuff = json.load(f)
    auth = tweepy.OAuthHandler(stuff["key"], stuff["secret"])
    auth.set_access_token(stuff["access token"], stuff["access token secret"])
    return tweepy.API(auth)

def rawdata(api: tweepy.API, obj: tweepy.User):
    return {
        "user": obj.screen_name,
        "followers": obj.followers_count,
        "friends": obj.friends_count,
        "statuses": obj.statuses_count,
        # "top10": list(map(lambda x: x.full_text, api.user_timeline(obj, count=10, tweet_mode="extended")))
        "top10": api.user_timeline(obj)
    }

def push_user(api: tweepy.API, user: str):
    obj = api.get_user(user)
    users.append(obj)
    rawds.append(rawdata(api, obj))

def expand(api: tweepy.API):
    user = users.popleft()
    for follower in api.followers(user):
        users.append(follower)
        rawds.append(rawdata(api, follower))

def main():
    api = setup()
    push_user(api, "@ezraklein")
    expand(api)
    print(list(rawds))

if __name__ == "__main__":
    main()