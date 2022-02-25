import time
from datetime import datetime
import tweepy
from django.conf import settings
from apscheduler.schedulers.background import BackgroundScheduler

REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'
access_token_url = "https://api.twitter.com/oauth/access_token"

consumer_key = settings.SOCIAL_AUTH_TWITTER_KEY
consumer_secret = settings.SOCIAL_AUTH_TWITTER_SECRET
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

def follow(request):
    access_key = "1417357878080331777-McGsmY3Hzq87TXXg9cWBXQMAUMbfdU"
    access_secret = "CmCgkbFSijdZVAJIuspgbJ9t2CQbotrMujfn9Bz3RQD8l"
                
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)      
    q = "#副業" #ここに検索キーワードを設定
    count = 10

    search_results = api.search_tweets(q=q, count=count)

    for result in search_results:
        # username = result.user._json['screen_name'] 
        tweet_id = result.id #ツイートのstatusオブジェクトから、ツイートidを取得
        user_id = result.user._json['id']
        # user = result.user.name #ツイートのstatusオブジェクトから、userオブジェクトを取り出し、名前を取得する                    # tweet = result.text #ツイートの内容を追加
        # time = result.created_at #ツイートの日時を取得
        try:
            api.create_favorite(tweet_id) #favする
            api.create_friendship(user_id = user_id) #フォローする
            time.sleep(5)
        except Exception as e:
            print(e)

def start():
    """
    Scheduling data update
    Run update function once every 12 seconds
    """
    scheduler = BackgroundScheduler()
   
    scheduler.add_job(follow, 'interval', seconds=10) # schedule
    scheduler.start()