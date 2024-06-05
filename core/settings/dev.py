from .base import *
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent


SECRET_KEY = "django-insecure-58x&*3)=mkp0bc8+80c$vr@s^vhn5ewfljgap+k_s%jtxqu$mh"
DEBUG = True

ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = ["http://localhost:3000"]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

CORS_ALLOW_CREDENTIALS = True

INTERNAL_IPS = [
    "127.0.0.1",
]

SITE_NAME = "plantx"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
