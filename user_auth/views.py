from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from social_django.models import UserSocialAuth
from django.conf import settings
import tweepy
import json

from requests_oauthlib import OAuth1Session
import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

from user_auth.models import User

REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"

consumer_key = settings.SOCIAL_AUTH_TWITTER_KEY
consumer_secret = settings.SOCIAL_AUTH_TWITTER_SECRET
        
# トップページ（認証へのリンクを設置するページ）
def index(request):
    return render(request, 'user_auth/login.html')

def top(request):
    # return render(request, 'user_auth/top.html') 
    if request.user.is_authenticated:
        # oauth_client = OAuth1Session(consumer_key, client_secret=consumer_secret)
        # try:
        #     resp = oauth_client.fetch_request_token(REQUEST_TOKEN_URL)
        #     oauth = OauthToken(oauth_token=resp.get('oauth_token'),
        #     oauth_token_secret=resp.get('oauth_token_secret'))
        
        #     oauth.save()
        # except ValueError:
        #     print ('認証失敗しました')
        #     return
        # return  oauth_client.authorization_url(AUTHORIZATION_URL)
        
        user = UserSocialAuth.objects.get(user_id=request.user.id)
        access_token = user.extra_data['access_token']['oauth_token']
        access_secret = user.extra_data['access_token']['oauth_token_secret']
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        api = tweepy.API(auth,wait_on_rate_limit = True)
        timeline = api.home_timeline()
        
        User = {
            'screen_name' : user.access_token.screen_name,
            'user_id' : user.access_token.user_id,
            'user_name' : user.user_name,
            'user_img' : user.access_token.user_img,
            'follow' : user.access_token.friends_count,
            'follower' : user.access_token.followers_count, 
        }
        
        # data = accounts()
        # data.screen_name = user.access_token.screen_name
        # data.user_id = user.access_token.user_id
        # data.user_name = user.access_token.user_name
        # data.user_img = user.access_token.user_img
        # data.user_text = user.access_token.user_text
        # data.user_created_at = user.access_token.created_at
        # data.save()
                
        return render(request,'user_auth/top.html', User, {'user': user, 'timeline': timeline})
    else:
        return render(request,'user_auth/top.html')

def signin(request):
    # request token取得
    callback_uri = "https://127.0.0.1:8000/user/complete/twitter/"
    oauth = OAuth1Session(
            consumer_key,
            client_secret=consumer_secret,
            callback_uri=callback_uri)
    request_token_url = "https://api.twitter.com/oauth/request_token"
    response = oauth.fetch_request_token(request_token_url)

    # 認証用URL作成
    redirect_url = "https://api.twitter.com/oauth/authenticate?oauth_token=" + response["oauth_token"]

    # 認証へリダイレクト
    return redirect(redirect_url)

def callback(request):
    access_token = user.extra_data['access_token']['oauth_token']
    access_secret = user.extra_data['access_token']['oauth_token_secret']
    request_token = request.GET["oauth_token"]; # リクエストトークンは以前と同じもの
    verifier = request.GET["oauth_verifier"];
    oauth = OAuth1Session(
            consumer_key,
            client_secret=consumer_secret,
            resource_owner_key=request_token,
            verifier=verifier)
    
    access_token_url = "https://api.twitter.com/oauth/access_token"
    # アクセストークン取得
    response = oauth.fetch_request_token(access_token_url)

    # DBに追加or更新
    try:
        # レコードが存在するか確認
        user = User.objects.get(id=response["user_id"])
        if user.access_token != response["oauth_token"]:
            # アクセストークンが変わった場合更新
            user.access_token = response["oauth_token"]
            user.access_token_secret = response["oauth_token_secret"]
            user.save()
    except User.DoesNotExist:
        # 存在しなかったら追加
        user = User()
        user.id = response["user_id"]
        user.access_token = response["oauth_token"]
        user.access_token_secret = response["oauth_token_secret"]
        user.save()

    # セッションにトークンを保存
    request.session["access_token"] = response["oauth_token"]

    # リダイレクト
    return redirect("user_auth.views.top_page")

@login_required
def top_page(request):
    user = UserSocialAuth.objects.get(user_id=request.user.id)
    
    return render(request,'user_auth/top.html',{'user': user})
# def top_page(request):
    
#     user = UserSocialAuth.objects.get(user_id=request.user.id)
#     request_token = request.GET["oauth_token"];
#     verifier = request.GET["oauth_verifier"];
    
#     oauth_client = OAuth1Session(
#         consumer_key, client_secret=consumer_secret,
#         resource_owner_key=request_token,
#         verifier=verifier
#         )

#     access_token_url = "https://api.twitter.com/oauth/access_token"
#     # アクセストークン取得
    
#     # request.session["access_token"] = response["oauth_token"]
    
#     # return redirect("user_auth.views.top")
    
#     # return  oauth_client.authorization_url(AUTHORIZATION_URL)
        
#     # User = {
#     #     'screen_name' : user.access_token.screen_name,
#     #     'user_id' : user.access_token.user_id,
#     #     'user_name' : user.user_name,
#     #     'user_img' : user.access_token.user_img,
#     #     'follow' : user.access_token.friends_count,
#     #     'follower' : user.access_token.followers_count, 
#     # }
    
#     return render(request,'user_auth/top.html', {'user': user})
