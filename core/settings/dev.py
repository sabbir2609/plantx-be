import os
from dotenv import load_dotenv
from .base import *  # noqa: F403
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv()


SECRET_KEY = os.environ["SECRET_KEY"]
DEBUG = True

ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "https://sabbir2609.pythonanywhere.com",
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://sabbir2609.pythonanywhere.com",
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


MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"
