from .base import *

DEBUG = True

DATABASES = {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
}