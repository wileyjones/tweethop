# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


#setting keys
import os
consumer_key = os.environ[consumer_key]
consumer_secret = os.environ[secret_key]
access_token = os.environ[access_token]
access_token_secret = os.environ[access_token_secret]


#tweepy setup
import tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text
