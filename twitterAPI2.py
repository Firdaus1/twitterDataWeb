__author__ = 'Firdaus'
import tweepy
from flask import Flask
from flask import render_template
import flask
import os
app = Flask(__name__)



def isEnglish(s):
    try:
        s.encode('ascii')
    except UnicodeEncodeError:
        return False
    else:
        return True



consumer_key = 'YNkO8iag20pDhczNMKpsyibUK'
consumer_secret = 'Y5jL5mkrOe4kd5YU6pahFxAdF93jZAAo1jp8Lewf1aCZg0LdgR'
access_token = '766031551352147968-wD7cJDuTKFfwkA3B7aL87UUCr8yt5r1'
access_token_secret = 'CbNgyRM8SW1meXusjIar81IhuRk1t4urMCu3mEhTDCndC'
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

trends1 = api.trends_place(1) # from the end of your code
# trends1 is a list with only one element in it, which is a
# dict which we'll put in data.
data = trends1[0]
# grab the trends
trends = data['trends']
trends = sorted(trends, key=lambda k: 0 if k['tweet_volume'] is None else k['tweet_volume'])

labels = []
data = []
for name in trends:
    if isEnglish(name['name']) and name['tweet_volume'] is not None:
        if (name['tweet_volume'] > 20000):
            labels.append(name['name'])
            data.append(name['tweet_volume'])

@app.route('/')
def homePage():
    return flask.render_template('index.html', tempLabels=labels, tempData=data)

if __name__ == '__main__':
    app.run(debug=True)