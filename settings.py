# -*- coding: utf-8 -*-
import psycopg2
import logging
import os

try:
    import colorama
except:
    from pip._vendor import colorama

colorama.init()

print(
    "\033[33m"
    "You're using a dev settings file. It includes django rosetta (in order "
    " for dev to update translations) that is only useful for dev. "
    "If you're a developper you need to 'pip3 install -e \".[dev]\"', "
    "If you want to use the app without doing your own settings you should"
    " remove django-rosetta from the installed apps in the settings."
    "\033[39m"
)

# ALLOWED_HOST = ["https://6e4c5806.ngrok.io","http://127.0.0.1:8000/survey/"]
ALLOWED_HOSTS = ['*'] #https://ohl1.herokuapp.com/
DEBUG = False
ROOT = os.path.dirname(os.path.abspath(__file__))
CSV_DIR = os.path.join(ROOT, "csv")

logging.basicConfig(
    level=logging.DEBUG,
    format="%(name)s.%(funcName)s() l.%(lineno)s -\033[32m %(message)s \033[39m",
)

if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
else:
    DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "ohldb",
        "USER": "jack",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "",
    }
}


# DATABASES = {
#     "default": {
#         "ENGINE": #"django.db.backends.sqlite3",
#         'django.db.backends.postgresql_psycopg2',
#         #"django.db.backends.sqlite3", #'postgresql_psycopg2',
#         # 'mysql', 'sqlite3' or 'oracle'
#         "NAME": "survey.db",  # Or path to database file if using sqlite3
#         "USER": "",  # Not used with sqlite3
#         "PASSWORD": "",  # Not used with sqlite3.
#         "HOST": "",  # Set to empty string for localhost. Not used with sqlite3
#         "PORT": "",  # Set to empty string for default. Not used with sqlite3
#     }
# }

USER_DID_NOT_ANSWER = "Left blank"

TEX_CONFIGURATION_FILE = os.path.join(ROOT, "doc", "example_conf.yaml")
SURVEY_DEFAULT_PIE_COLOR = "red!50"

CHOICES_SEPARATOR = ","

LANGUAGE_CODE = "en-us"
SITE_ID = 1
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_URL = "/media/"
STATIC_URL = "/static/"

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(ROOT, "media")
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

DEBUG_ADMIN_NAME = "test_admin"
DEBUG_ADMIN_PASSWORD = "test_password"

STATICFILES_DIRS = (os.path.join(ROOT,'assets'),)


STATICFILES_DIRS = [os.path.normpath(os.path.join(ROOT, "..", "survey", "static"))
                    
]

# Make this unique, and don't share it with anybody.
SECRET_KEY = '0+bc1mx-$7y)b&5#@80w5ja0zt2w=5*fr-cqa28ptp&gpzg0@b'
#SECRET_KEY = os.environ.get("SECRET_KEY", "some value if your key is not in the environment")

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(ROOT, "survey", "templates"),
            os.path.join(ROOT, "dev", "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "debug": DEBUG,
            "context_processors": [
                # Default
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]

MIDDLEWARE = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)

ROOT_URLCONF = "urls"
WSGI_APPLICATION = "wsgi.application"

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.admindocs",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "survey",
    
)

LOCALE_PATHS = (os.path.join(ROOT, "survey", "locale"),)
LANGUAGE_CODE = "en"
LANGUAGES = (
    ("en", "english"),
    ("ru", "russian"),
    ("es", "spanish"),
    ("fr", "french"),
    ("ja", "Japanese"),
    ("zh", "Chinese"),
)

LOGIN_REDIRECT_URL = "/"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        }
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        }
    },
}
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OHL.settings")
