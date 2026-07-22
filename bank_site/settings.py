"""
Django settings for bank_site project.
"""

import os 
from dotenv import load_dotenv
load_dotenv()
import django
from pathlib import Path
import sys
import dj_database_url
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Cloudinary configuration
cloudinary.config(
    cloud_name="dlzn0moho",
    api_key="563396395915366",
    api_secret="pCSSrLNvxfFSEzY4ZnaOiF5u93o"
)

# Quick-start development settings - unsuitable for production
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-os%ceh%!b_zte(60bvi9)pujn1v#lyuh^u4l!hr+_-5)rmf&9-')
DEBUG = os.environ.get('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')

CSRF_TRUSTED_ORIGINS = os.environ.get('CSRF_TRUSTED_ORIGINS', '').split(',') if os.environ.get('CSRF_TRUSTED_ORIGINS') else []
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Application definition
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'cloudinary',
    'cloudinary_storage',  
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'BankApp',
    'django_use_email_as_username.apps.DjangoUseEmailAsUsernameConfig',
    'custom_user.apps.CustomUserConfig',
    'django.contrib.humanize',
]

AUTH_USER_MODEL = 'custom_user.User'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bank_site.urls'

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
                'BankApp.context_processors.site_icons',
            ],
        },
    },
]

WSGI_APPLICATION = 'bank_site.wsgi.application'
# Database configuration
import os
import dj_database_url

DATABASE_URL = os.environ["DATABASE_URL"]  # Raises an error if not set

DATABASES = {
    "default": dj_database_url.config(
        default=DATABASE_URL,
        conn_max_age=600,
        ssl_require=True,
    )
}

DATABASES["default"]["OPTIONS"] = {
    "client_encoding": "UTF8",
    "connect_timeout": 10,
}
# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
# Static files (CSS, JavaScript, Images)


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Get Django's admin static path
django_path = os.path.dirname(django.__file__)
admin_static = os.path.join(django_path, 'contrib', 'admin', 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    admin_static,  # Add Django's admin static files
]

# WhiteNoise configuration
WHITENOISE_USE_FINDERS = True
WHITENOISE_MANIFEST_STRICT = False
WHITENOISE_ALLOW_ALL_ORIGINS = True
WHITENOISE_ROOT = STATIC_ROOT

# Static files storage
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'trustbankapex@gmail.com'
EMAIL_HOST_PASSWORD = 'egmt ojnz uqbg ppjw'
DEFAULT_FROM_EMAIL = 'Apex Trust Bank <trustbankapex@gmail.com>'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
