# -*- coding: utf-8 -*-

from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': './default.db',                      # Or path to database file if using sqlite3.
    },
}

#DATABASES = {
    #'default': {
        #'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        #'NAME': 'deebate',                      # Or path to database file if using sqlite3.
        #'USER': 'root',                      # Not used with sqlite3.
        #'PASSWORD': '',                  # Not used with sqlite3.
        #'HOST': '127.0.0.1',                      #  ATTENZIONE: con localhost non va
        #'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        #'OPTIONS': {
               #"init_command": "SET storage_engine=INNODB",
        #},
    #},
    #'stefano': {
        #'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        #'NAME': './stefano.db',                      # Or path to database file if using sqlite3.
        ##'USER': 'root',                      # Not used with sqlite3.
        ##'PASSWORD': 'opineo',                  # Not used with sqlite3.
        ##'HOST': 'opineo',                      # Set to empty string for localhost. Not used with sqlite3.
        ##'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    #},
#}



