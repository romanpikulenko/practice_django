"""
Django settings for practice_django project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

from django.contrib.messages import constants as messages
from dotenv import load_dotenv

# django-debug-toolbar
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
# End django-debug-toolbar


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# python-dotenv
# https://pypi.org/project/python-dotenv/
# .env is the setting file in the root of the project
# Loading Env

env_path = BASE_DIR / ".env"
load_dotenv(dotenv_path=env_path)

# End python-dotenv


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = "django-insecure-2!@l!nmbous%g!vpf=-z!2*h-xk)aqy-i@o&3vkdx_nd*+mi5e"
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG")

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    # django-allauth
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.github",
    # https://django-crispy-forms.readthedocs.io/en/latest/install.html
    "crispy_forms",
    # https://django-ckeditor.readthedocs.io/en/latest/#installation
    "ckeditor",
    # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
    "debug_toolbar",
    # https://channels.readthedocs.io/en/stable/installation.html
    # "channels",
    # https://django-extensions.readthedocs.io/en/latest/installation_instructions.html
    "django_extensions",
    # Our apps
    "blog.apps.BlogConfig",
    # End our apps
    # https://pypi.org/project/django-cleanup/
    # Note: Order of INSTALLED_APPS is important. To ensure that exceptions inside other apps’ signal handlers
    # do not affect the integrity of file deletions within transactions, django_cleanup should be placed last in INSTALLED_APPS.
    "django_cleanup.apps.CleanupConfig",
]

SITE_ID = 1

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "practice_django.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# django-allauth
# https://django-allauth.readthedocs.io/en/latest/installation.html

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
]

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
    },
    "github": {"SCOPE": ["user", "profile", "read:org"]},
}

# End django-allauth

WSGI_APPLICATION = "practice_django.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db_1.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"
STATICFILES_DIRS = [
    BASE_DIR / "other_static",
]
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-MEDIA_ROOT
MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# crispy-forms
# https://django-crispy-forms.readthedocs.io/en/latest/install.html

# CRISPY_TEMPLATE_PACK = "uni_form"
CRISPY_TEMPLATE_PACK = "bootstrap4"

# End crispy-forms

# https://docs.djangoproject.com/en/4.1/ref/settings/
# The URL or named URL pattern where requests are redirected after login
# when the LoginView doesn’t get a next GET parameter.
LOGIN_REDIRECT_URL = "blog-home"

# The URL or named URL pattern where requests are redirected for login when using the login_required() decorator,
# LoginRequiredMixin, or AccessMixin.
LOGIN_URL = "account-login"

# ckeditor
# https://django-ckeditor.readthedocs.io/en/latest/#installation

CKEDITOR_CONFIGS = {
    "default": {
        "width": "auto",
    }
}

# End ckeditor

# channels
"""
ASGI_APPLICATION = "practice_django.routing.application"

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    }
}
"""
# End channels

# Email

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_USE_TLS = True
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_HOST_USER = os.getenv("EMAIL_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_PASS")

# End Email

GOOGLE_RECAPTCHA_SECRET_KEY = os.getenv("GOOGLE_RECAPTCHA_SECRET_KEY")

MESSAGE_TAGS = {
    messages.DEBUG: "alert-secondary",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}

# remove in production
# https://docs.djangoproject.com/en/3.1/topics/async/#async-safety
# Jupyter shell doesn't work without the setting below
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
