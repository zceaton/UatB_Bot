import tweepy, time, sys

CONSUMER_KEY = 'LjFGyReJkF4716BTuNm1Jo59v'
CONSUMER_SECRET = '9MyGb0e9TfTBqDpQ3DSP6sltBbpioeceDU1Zh8MRntNVWHTmhx'
ACCESS_KEY = '800524108735729664-2e0v0TybtuteMWfjHV4aa8e2KtKNGqn'
ACCESS_SECRET = 'SB75lvIBiqoBVNed1FZd8pdjVTqBEsE2Rhi7CmVytmLly'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

query1 = '"University of Buffalo"'
query2 = '"Buffalo University"'
replyTweet = 'I believe you meant the University AT Buffalo'
fRead = open('repliedIDs.txt', 'r')
line = fRead.readline()
counter = 0
if not line:
    line = str(0)

for tweet in tweepy.Cursor(api.search,q=query1,since_id=long(line)).items(5):
    replyTweet1 = '@' + tweet.user.screen_name + " " + replyTweet
    api.update_status(status=replyTweet, in_reply_to_status_id=tweet.id)
    if counter == 0:
        fWrite = open('repliedIDs.txt', 'w')
        fWrite.write(str(tweet.id))
        fWrite.close()
    counter = counter + 1
