# -*- coding: utf-8 -*-

from .base import *

DEBUG = True  # False - TODO: sistemare quando andrà davvero in produzione; per ora gli errori devono essere visibili

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'deebate',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'nus3eg7k',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        'OPTIONS': {
               "init_command": "SET storage_engine=INNODB",
        },
    }
}

SITE_ID = 2

DEFAULT_FROM_EMAIL = "info@deebate.it"

TWITTER_CONSUMER_KEY         = 'TOGdddhwI7n6Y0tapakmSw'
TWITTER_CONSUMER_SECRET      = 'qpsAa1WfexAY8rwjQrPyA6XmF8UdyUN2W3BFxgQEA'

FACEBOOK_APP_ID              = '293656037414177'
FACEBOOK_API_SECRET          = '4f1a9c10b6468de1e6f5f5ae469904f5'

GOOGLE_OAUTH2_CLIENT_ID      = '7727474150372.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET  = 'b1J1o0jClmB7rrFzamMLRtuF'

# capire se in produzione possiamo evitare il giro via internet e andare di localhost, ma direi di si
EMAIL_HOST = 'mail.4d3.it'
EMAIL_HOST_USER = 'noreply@deebate.it'
EMAIL_HOST_PASSWORD = 'd33b4t3mail'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
