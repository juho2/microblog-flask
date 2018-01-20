# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__)) 

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

   
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
WHOOSH_BASE = os.path.join(basedir, 'search.db')

# mail server settings
# to test, run with debug=False, cmd -> python -m smtpd -n -c DebuggingServer localhost:25
MAIL_SERVER = 'asmtp@mail.dk'
MAIL_PORT = 587
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

# administrator list
ADMINS = ['juho@mail.dk']

# pagination
POSTS_PER_PAGE = 3
MAX_SEARCH_RESULTS = 50

# available languages
LANGUAGES = {
    'en': 'English',
    'es': 'Español'
}