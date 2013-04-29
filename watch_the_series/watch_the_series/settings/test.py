# -*- coding: utf-8 -*-

from .base import *

DEBUG = True

DATABASES = {'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': '%s/test.db' % ROOT_ABSOLUTE, # Or path to database file if using sqlite3.
    }}

# Set your DSN value
RAVEN_CONFIG = {
    'dsn': 'https://adeaca2673874538a4b46f013e6d7aa4:4fb6cb41269f436580fae3345ea5b2a3@app.getsentry.com/5772',
}

#JENKINS_TEST_RUNNER='django_jenkins.nose_runner.CINoseTestSuiteRunner'

JENKINS_TASKS = (
    'django_jenkins.tasks.run_pylint',
    #'django_jenkins.tasks.with_coverage',
    #'django_jenkins.tasks.django_tests',
    #'django_jenkins.tasks.run_sloccount',
    'django_jenkins.tasks.run_pyflakes',
    'django_jenkins.tasks.run_pep8',
    #'django_jenkins.tasks.run_flake8',
    #'django_jenkins.tasks.run_graphmodels',
)


# Add raven to the list of installed apps
INSTALLED_APPS = INSTALLED_APPS + (
    # ...
    'raven.contrib.django.raven_compat',
)

import logging
logging.basicConfig()
south_logger=logging.getLogger('south')
south_logger.setLevel(logging.INFO)
selenium_logger=logging.getLogger('selenium')
selenium_logger.setLevel(logging.INFO)
logger = logging.getLogger('sentry.errors')
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())
#EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
#EMAIL_FILE_PATH = ROOT_PROJECT_INTERNAL + '\\tmp\\emails' # change this to a proper location


# Deebate.local app
# https://dev.twitter.com/apps
TWITTER_CONSUMER_KEY         = 'VJugn4SvSQ6VZALjV0XbA'
TWITTER_CONSUMER_SECRET      = 'IVvxU4WimfHZTKY905DLXYwleL7WOwVkSVPzlNPx68'

FACEBOOK_APP_ID              = '224280657702861'
FACEBOOK_API_SECRET          = '26cdc01be15795c0ec6da51cdf358c0a'

# https://code.google.com/apis/console/?hl=it&pli=1#project:727474150372:access
GOOGLE_OAUTH2_CLIENT_ID      = '77551104922.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET  = 'ece1LmkSiDoW9PgisnHU6r8s'

FACEBOOK_TEST_USER = "wvylpmj_letuchyman_1359061987@tfbnw.net"
FACEBOOK_TEST_PASSWORD = "deebate"
FACEBOOK_TEST_NOME_VISUALIZZATO = "Mike Bike"

TWITTER_TEST_USER = "deebatetestuser@gmail.com"
TWITTER_TEST_PASSWORD = "deebate"
TWITTER_TEST_NOME_VISUALIZZATO = "Mike Bike"

GOOGLE_TEST_USER = "deebatetestuser"
GOOGLE_TEST_PASSWORD = "deebate!"
GOOGLE_TEST_NOME_VISUALIZZATO = "Mike Bike"

#SOCIAL_AUTH_RAISE_EXCEPTIONS = True

