# python twitter 'conversation' application
# summary: read @ messages, respond.

import configparser
import json

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API

from nltk.chat import eliza

# read twitter config file
config = configparser.ConfigParser()
config.read('twitter.config')

# assign keys & secrets
consumer_key = config.get('APIKEY', 'MY_CONSUMER_KEY')
consumer_secret = config.get('APIKEY', 'MY_CONSUMER_SECRET')

# assign token & secret
access_key = config.get('TOKEN', 'MY_ACCESS_TOKEN_KEY')
access_secret = config.get('TOKEN', 'MY_ACCESS_TOKEN_SECRET')

# assign rule & screen name
stream_rule = config.get('APP', 'RULE')
screen_name = config.get('APP', 'SCREEN_NAME').lower()
user_id = config.get('APP', 'USER_ID')

# setup OAuth connection
oauth = OAuthHandler(consumer_key, consumer_secret)
oauth.set_access_token(access_key, access_secret)

# setup twitter API
twitterAPI = API(oauth)

# setup eliza NLTK
chathandler = eliza.Chat(eliza.pairs, eliza.reflections)

#########################################################


class replyToTweet(StreamListener):

    def on_data(self, data):
        print('=' * 72)
        print(data)
        print('='*72)

        tweet = json.loads(data.strip())

        retweeted = tweet.get('retweeted')
        from_self = tweet.get('user', {}).get('screen_name') == user_id

        print('=' * 72)
        print(retweeted)
        print(from_self)
        print('=' * 72)

        if retweeted is not None and not retweeted and not from_self:
            tid = tweet.get('id_str')
            user_screen = tweet.get('user', {}).get('screen_name')
            tweetTxt = tweet.get('text')

            response = chathandler.respond(tweetTxt)

            replyTxt = '@' + user_screen + ' ' + response

            # is our response > 140 characters
            if len(replyTxt) > 140:
                replyTxt = replyTxt[0:139] + '...'

            print('Tweet ID: ' + tid)
            print('From: ' + user_screen)
            print('Tweet Text: ' + tweetTxt)
            print('Response Text: ' + replyTxt)

            # send our response
            twitterAPI.update_status(status=replyTxt, in_reply_to_status_id=tid)

    def on_error(self, status_code):
        print(status_code)


#########################################################

if __name__ == '__main__':
    print("Running conversation...")
    streamListener = replyToTweet()
    twitterStream = Stream(oauth, streamListener)
    twitterStream.userstream(_with='user')

    # END
