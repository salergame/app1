"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

from django.conf.global_settings import MEDIA_URL

SITE_ID = 1

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2apt!#m1d-^r(0w83d_o5gzmmfjd0jg!)t2&u#3k+!(!10&cy_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
    
    "rest_framework",
    "debug_toolbar",
    "django_filters",
    
    'main',
    'goods',
    'users',
    'carts',
    'orders',
    'api',
    'courier',
    
    ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    

    
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'home',
        'USER': 'home',
        'PASSWORD': 'home',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Almaty'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR/'static',
    ]

MEDIA_URL = 'media/'

MEDIA_ROOT = BASE_DIR / 'media'

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    "home",
    "localhost"
    # ...
]

LOGIN_REDIRECT_URL = '/'


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
<<<<<<< HEAD
AUTH_USER_MODEL = 'users.User'
LOGIN_URL = '/user/login/'

REST_FRAMEWORK = {
    'PAGE_SIZE' : 3
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]   

SOCIALACCOUNT_PROVIDERS = {
    'github': {
        # For each OAuth based provider, either add a ''SocialApp''
        # (''socialaccount'' app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '2560a722bf933219c4d4',
            'secret': 'c9d75ce966f76617c210be7e51e6f79fea501fef',
            'key': ''
        }
    },
    'google': {
        # For each OAuth based provider, either add a ''SocialApp''
        # (''socialaccount'' app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '946847496404-h009iu4p62vof55at5pl7a16tchh2qhv.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        }
    },
}

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_PORT = 25
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'salergame07@gmail.com'
EMAIL_HOST_PASSWORD = 'ogjm ujcx zwzq tbbz'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_FILE_PATH = BASE_DIR / "emails"

GOOGLE_MAP_API_KEY = 'AIzaSyADfCtqkBiMxMGxkYQIRoKanj4uW2n1L-A'
MAP_WIDGETS = {
 "GooglePointFieldWidget": (
 ("zoom", 15),
 ("mapCenterLocationName", "amsterdam"),
 ("GooglePlaceAutocompleteOptions", {'componentRestrictions': {'country': 'nl'}}),
 ("markerFitZoom", 12),
 ),
 "GOOGLE_MAP_API_KEY": GOOGLE_MAP_API_KEY
}
=======
>>>>>>> 7203c0d3ca24d97ad35e4406b64f3838b5a5f355
