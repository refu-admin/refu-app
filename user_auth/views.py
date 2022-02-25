from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.conf import settings
import tweepy
import json
import twitter
import time
import logging

from django.core.management.base import BaseCommand

from requests_oauthlib import OAuth1Session
import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from user_auth.models import OAuthTokenTemp
from allauth.socialaccount.models import SocialAccount
from .forms import TweetForm

REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'
access_token_url = "https://api.twitter.com/oauth/access_token"

consumer_key = settings.SOCIAL_AUTH_TWITTER_KEY
consumer_secret = settings.SOCIAL_AUTH_TWITTER_SECRET
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        
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
    
# @login_required
class Top_page_View(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'

    logger = logging.getLogger(__name__)
    template_name = 'user_auth/top.html'
    model = SocialAccount
    context_object_name = 'accounts'
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
    # logger.info("SocialAccount.extra_data['access_token']['oauth_token']")
        access_key = "1417357878080331777-McGsmY3Hzq87TXXg9cWBXQMAUMbfdU"
        access_secret = "CmCgkbFSijdZVAJIuspgbJ9t2CQbotrMujfn9Bz3RQD8l"
        
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth)      
        user_id='1417357878080331777'
        user = api.get_user(user_id = user_id)
        
                        
        context = {
            "screen_name" : user.screen_name,
            "user_name" : user.name,
            "user_id" : user.id_str,
            "followers_count" : user.followers_count,
            "friends_count" : user.friends_count,
            "FFrate": int(user.followers_count/user.friends_count*100),
            "image" : user.profile_image_url, 
        }
        
        return context

    
class Base_page_View(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    template_name = 'user_auth/base.html'
    model = SocialAccount
    context_object_name = 'accounts'
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
    # logger.info("SocialAccount.extra_data['access_token']['oauth_token']")
        access_key = "1417357878080331777-McGsmY3Hzq87TXXg9cWBXQMAUMbfdU"
        access_secret = "CmCgkbFSijdZVAJIuspgbJ9t2CQbotrMujfn9Bz3RQD8l"
        
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth)      
        user_id='1417357878080331777'
        user = api.get_user(user_id = user_id)
        
        # try:
#             access_key = "1417357878080331777-McGsmY3Hzq87TXXg9cWBXQMAUMbfdU"
#             access_secret = "CmCgkbFSijdZVAJIuspgbJ9t2CQbotrMujfn9Bz3RQD8l"
#             auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#             auth.set_access_token(access_key, access_secret)
#             api = tweepy.API(auth)
#             profile = api.get_user(id=SocialAccount.extra_data['id']['user_id'])
#             oauth = OAuthTokenTemp(
#                 user_id = '1417357878080331777', #uid
#                 name = profile.screen_name, #アカウント名 @*
#                 # image = profile.profile_image_url, #アイコン画像のURL
#                 # tweet_count = profile.statuses_count, #ツイート数
#                 friends_count = profile.friends_count, #フォロー数
#                 followers_count = profile.followers_count, #フォロワー数
#                 # description = profile.describe_option, #profile info
#             )
#             oauth.save()
        
        context = {
            "screen_name" : user.screen_name,
            "user_name" : user.name,
            "user_id" : user.id_str,
            "followers_count" : user.followers_count,
            "friends_count" : user.friends_count,
            "image" : user.profile_image_url, 
        }
        return context
    # def get_queryset(self):
        
    #     user_obj = self.request.user
    #     if user.is_authenticated:
    #         qs =OAuthTokenTemp.objects.filter(user=user_obj)
    #     else:
    #         qs = OAuthTokenTemp.objects.none()
    #     return qs