# -*- coding: utf-8 -*-

import tweepy, time, sys

#argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = ' IicoNuhSOlY6ciZ9bdzzbva8s'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = ' Cmr35qwqd1n06tdDtYmRzbqmYvZFXQmrLmsWDenKf3GYZTFBXO'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '3317742490-VCmb9dUCXxtiKjOVBigRfDWQEko34TOJmRqZB9W'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'OIunphd5UoKe8kMFAAGoHnOuJ5GXF2ROceE39feBlZ8eS'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open('text.txt','r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    time.sleep(900)#Tweet every 15 minutes