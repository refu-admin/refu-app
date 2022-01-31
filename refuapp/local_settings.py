import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SOCIAL_AUTH_TWITTER_KEY = 'HP2t2eCUjG7GiMJJUfbMMgUTd'
SOCIAL_AUTH_TWITTER_SECRET = 'k1UBmYj8nFikP0GJiX5YfBwkTat2ty3e4TE9AS90cl7eh0kD8R'

ALLOWED_HOSTS = []

DEBUG = True
