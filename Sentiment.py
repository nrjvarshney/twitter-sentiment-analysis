
# coding: utf-8

# In[1]:


import re 
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob


# In[16]:


# copy keys from here https://developer.twitter.com/en/apps
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# In[26]:


search_term = "Microsoft"
tweets = api.search(q= search_term, count = 100)


# In[30]:


positive = 0
negative = 0
neutral = 0
polarity = 0


# In[31]:


for tweet in tweets:
#     print (tweet.text)
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity
    
    if(analysis.sentiment.polarity == 0):
        neutral += 1
    if(analysis.sentiment.polarity > 0):
        positive += 1
    if(analysis.sentiment.polarity < 0):
        negative += 1

print(positive,negative,neutral)

