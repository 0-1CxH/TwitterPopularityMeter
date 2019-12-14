# -*- coding: utf-8 -*-

from __future__ import print_function
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

ACCESS_TOKEN = '1201278023472840705-vXvkf0jOOturE1Kt6WxbT5bdMW7afP'
ACCESS_SECRET = '1R70xgn5OOBHYHxVcmCdr0vvX5DRdTzAuhaHdvIbT9hYJ'
CONSUMER_KEY = 'mUeXO93OhVbf8EqCOg2PmCKD4'
CONSUMER_SECRET = 'fJTzWcyPMSYvtiiFQZSK6x1Uf6FSV4HZEbg0sq9psU9H6im9Iz'

tweetDoc = open('twitterDoc.txt', 'w')

class listener(StreamListener):

    def on_data(self, data):
        print(data, file = tweetDoc) 
        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
twitterStream = Stream(auth, listener(),tweet_mode="extended")
twitterStream.filter(track="Christmas")

tweetDoc.close()
