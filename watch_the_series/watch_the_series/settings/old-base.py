# -*- coding: utf-8 -*-
# Django settings for deebate project.

import os, sys
import socket
from django.core.urlresolvers import reverse_lazy
from os.path import join, dirname, abspath, normpath

HOST_NAME = socket.gethostname()
PROJECT_NAME = "deebate"

ROOT_PROJECT_INTERNAL = normpath(join(dirname(abspath(__file__)), ".."))
ROOT_ABSOLUTE = normpath(join(ROOT_PROJECT_INTERNAL, "..", ".."))

sys.path.append(ROOT_ABSOLUTE) # così si può trovare core e deebate

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
     ('Alessandro Pelliciari', 'isac.newton@gmail.com'),
)

MANAGERS = ADMINS


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Rome'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html

LANGUAGE_CODE = 'it-IT'
#LANGUAGE_CODE = 'en-US'

ugettext = lambda s: s

LANGUAGES = (
    ('it', ugettext('Italian')),
    ('en', ugettext('English')),
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = join(ROOT_ABSOLUTE, "public", "media")


# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
# deprecated in 1.4
# ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    join(ROOT_ABSOLUTE, "public", "static"), #per servire i file statici in locale
    join(ROOT_ABSOLUTE, "public", "media"),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '$tc(tkrs3qvz5_)3$)h@u+5dn!v7oe0ap^g9rl#^r38pdm5d+('

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'core.middleware.JavascriptDefinerMiddleware',
    'core.middleware.ValidRefererMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',

)

ROOT_URLCONF = 'deebate.urls'


TEMPLATE_DIRS = (
    join(ROOT_PROJECT_INTERNAL, 'registration/templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'south', #migrations
    'registration', #django-registration
    'django_extensions',
    'sorl.thumbnail',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'django_js_utils',
    'debug_toolbar',
    'social_auth',
    'mathfilters',
    'rosetta',
    'django_jenkins',
    'django_nose',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

AUTHENTICATION_BACKENDS = (
  #  'django.contrib.auth.backends.ModelBackend',
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.google.GoogleOAuthBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    'social_auth.backends.google.GoogleBackend',
    'deebate.backends.EmailAuthBackend',
)

# auth profiles

#AUTH_PROFILE_MODULE = 'core.Utente'

# registration settings

ACCOUNT_ACTIVATION_DAYS = 999999 # One-Week activation window; you may, of course, use a different value.

# in locale non si inviano mail, oppure va fatto con gmail

TEMPLATE_CONTEXT_PROCESSORS = (
"django.contrib.auth.context_processors.auth",
"django.core.context_processors.debug",
"django.core.context_processors.i18n",
"django.core.context_processors.media",
"django.core.context_processors.static",
"django.contrib.messages.context_processors.messages",
"django.core.context_processors.request",
"core.context_processors.frontend",
'social_auth.context_processors.social_auth_backends',
)

SERIALIZATION_MODULES = {
    'json-pretty': 'deebate.serializers.json_pretty'
}

# solr-thumbnail

THUMBNAIL_DEBUG = DEBUG

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)

DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False
        }

INTERNAL_IPS = ('128.0.0.1',) # stop

###############################################################################
##### SOCIAL AUTH
###############################################################################

FACEBOOK_AUTH_EXTRA_ARGUMENTS = {'display': 'popup'}

FACEBOOK_EXTENDED_PERMISSIONS = ['email',]

GOOGLE_OAUTH2_USE_UNIQUE_USER_ID = True

LOGIN_URL          = '/login-form/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL    = '/login-error/'

SOCIAL_AUTH_LOGIN_REDIRECT_URL = reverse_lazy('social_complete_auth')
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = reverse_lazy('social_complete_auth')
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = reverse_lazy('social_complete_auth')
SOCIAL_AUTH_BACKEND_ERROR_URL = reverse_lazy('social_error')
SOCIAL_AUTH_COMPLETE_URL_NAME  = 'socialauth_complete'

SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'

SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.misc.save_status_to_session',
    'core.pipeline.redirect_collegamento_account',
    #'app.pipeline.username',
    'core.pipeline.email_as_username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'core.pipeline.create_utente',
    'core.pipeline.aggiorna_dati_utente',
    'social_auth.backends.pipeline.misc.save_status_to_session',
    #'core.pipeline.complete_redirect',
)

#SOCIAL_AUTH_PROCESS_EXCEPTIONS = 'social_auth.utils.log_exceptions_to_messages'


SOCIAL_AUTH_UID_LENGTH = 223
SOCIAL_AUTH_NONCE_SERVER_URL_LENGTH = 200
SOCIAL_AUTH_ASSOCIATION_SERVER_URL_LENGTH = 135
SOCIAL_AUTH_ASSOCIATION_HANDLE_LENGTH = 125

# custom

SITE_LAYOUT = "frontend"

FRONTEND_ROOT = join(ROOT_PROJECT_INTERNAL, "public", "static", SITE_LAYOUT)

CUSTOMER_CARE_EMAIL = "supporto@deebate.it"
USER_PASSWORD_MIN_LENGTH = 6

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

SOUTH_TESTS_MIGRATE = False # To disable migrations and use syncdb instead
SKIP_SOUTH_TESTS = True # To disable South's own unit tests
