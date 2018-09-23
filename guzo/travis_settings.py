"""
Ethiopian Transport API
Settings for guzo project.
"""

__author__ = "Dawit Nida (dawit@dawitnida.com)"
__date__ = "Date: 18-11-2017"
__version__ = "Version: 1.0.0"
__Copyright__ = "Copyright: @dawitnida"

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7d4f^5s^0#wr_k#+72as*3znd3j@x8ge#opwrb#)))d_+tyr-h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', ]

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'rest_framework',  # Django rest framework
    'rest_framework_swagger',  # Django-swagger
    'dbbackup',  # Django-dbbackup
    'graphene_django',  # Graphene for GraphSQ
    'oauth2_provider',  # OAuth Provider
    'corsheaders',  # corsheaders
    'guzo.lightrail',  # Guzo app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'guzo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'guzo.wsgi.application'

CORS_ORIGIN_ALLOW_ALL = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'guzo_api.db'),
        'CONN_MAX_AGE': 500,
    },
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# ## Graphene setup

GRAPHENE = {
    'SCHEMA': 'guzo.lightrail.schema.schema',
    'MIDDLEWARE': (
        'graphene_django.debug.DjangoDebugMiddleware',
    )
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
    # 'PAGE_SIZE': 10
}

STATIC_URL = '/static/'

# ## Admin Configurations ########################
ADMINS = (
    ('Dawit Nida', 'dawit@dawitnida.com'),
)

DBBACKUP_STORAGE = 'dbbackup.storage.filesystem_storage'
DBBACKUP_STORAGE_OPTIONS = {'location': '/var/backups'}
