import tweepy
from textblob import TextBlob

def main():
    print("Analysing 'Hello! I am a meatball!'")
    t = TextBlob('Hello I am a meatball!')
    print(t.sentiment)

main()