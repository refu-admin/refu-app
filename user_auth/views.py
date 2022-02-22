from contextlib import ExitStack
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from paramiko import AuthenticationException
from social_django.models import UserSocialAuth
from django.conf import settings
import tweepy
import json
import twitter
import logging

from requests_oauthlib import OAuth1Session
import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)


from user_auth.models import OAuthTokenTemp
from .forms import TweetForm

REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'
access_token_url = "https://api.twitter.com/oauth/access_token"

consumer_key = settings.SOCIAL_AUTH_TWITTER_KEY
consumer_secret = settings.SOCIAL_AUTH_TWITTER_SECRET
        
# トップページ（認証へのリンクを設置するページ）
def index(request):
    return render(request, 'user_auth/login.html')
        
@login_required
def top_page(request):
    oauth_client = OAuth1Session(consumer_key, client_secret=consumer_secret)
    # user = UserSocialAuth.objects.get(user_id=request.user.id)
    
    # user_oauth_token = user.extra_data['access_token']['oauth_token']
    # user_oauth_token_secret = user.extra_data['access_token']['oauth_token_secret']
    
    # #Tweepyの設定
    # auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # auth.set_access_token(user_oauth_token, user_oauth_token_secret)
    # api = tweepy.API(auth ,wait_on_rate_limit = True)    
    # # timeline = api.home_timeline()
    
    # profile = tweepy.api.get_user(user_id = '1417357878080331777')
    # response = auth.fetch_request_token(access_token_url)

    # try: 

    #     oauth = OAuthTokenTemp(
    #         user_id = profile.user_id,
    #         oauth_token = user_oauth_token,
    #         oauth_token_secret = user_oauth_token_secret,
    #         name = profile.screen_name, 
    #         description = profile.description, 
    #         friends_count = profile.friends_count, 
    #         followers_count = profile.followers_count,
    #     )
    
    #     if  OAuthTokenTemp.objects.get(user.user_id != '1417357878080331777') :   
    #         oauth.save()
    #     # request.session["access_token"] = response["oauth_token"]
            
    #     # return render(request,'user_auth/top.html', {'user': user})
        
    #     # else:
    #     #     return render(request,'user_auth/top.html', {'user': user})
    # except tweepy.TweepError:
    #     print ('Error! Failed to get request token.')
        
    
    return render(request,'user_auth/top.html')
    

def tweet(request):
    form = TweetForm
    return redirect('user_auth/top.html')
