from .base import *

DEBUG = False

ADMINS = (
    ("Julio B", "julesc00@protonmail.com"),
)

ALLOWED_HOSTS = [
    "educationproject.com",
    "www.educationproject.com",
    ".educationproject.com"
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "education",
        "USER": "education",
        "PASSWORD": "education",
    }
}

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
