import os  # noqa: F401
from pathlib import Path

from dotenv import load_dotenv

from .base import *  # noqa: F403

BASE_DIR = Path(__file__).resolve().parent.parent.parent

load_dotenv()


SECRET_KEY = "4%kruhj1q6jo$+wrkt+djo5_m)13pi49_d25)r7th1z1wnco8l"
DEBUG = True

ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://192.168.1.2:3000",
    "http://192.168.1.6:3000",
    "http://192.168.1.7:3000",
    "http://192.168.1.8:3000",
    "http://localhost:3000",
    "https://viriditas.vercel.app/",
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://192.168.1.2:3000",
    "http://192.168.1.4:3000",
    "http://192.168.1.6:3000",
    "http://192.168.1.7:3000",
    "http://192.168.1.8:3000",
    "https://sabbir2609.pythonanywhere.com",
    "https://plantx-fe.vercel.app",
    "https://viriditas.vercel.app",
]

CORS_ALLOW_CREDENTIALS = True

INTERNAL_IPS = [
    "127.0.0.1",
    "192.168.1.8",
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


# Email configurations
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = "noreply@zenith.com"
