import os
from pathlib import Path

import dj_database_url
from dotenv import load_dotenv

from .base import *  # noqa: F403

# Load environment variables from .env file
BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR / ".env")

# Retrieve essential environment variables
SECRET_KEY = os.getenv("SECRET_KEY")

# Convert DEBUG to boolean
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "yes")

if DEBUG == "True":
    print("DEBUG is True in prod.py")

# Process WEBSITE_HOSTNAME
website_hostname = os.getenv("WEBSITE_HOSTNAME", "")
formatted_website_hostname = ",".join(
    [f'"{host}"' for host in website_hostname.split(",")]
)

# Set allowed hosts
ALLOWED_HOSTS = website_hostname.split(",") if website_hostname else []

# Process CORS_ALLOWED_ORIGINS
CORS_ALLOWED_ORIGINS = os.getenv("CORS_ALLOWED_ORIGINS", "").split(",")
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = [
    "GET",
    "POST",
]

INTERNAL_IPS = ["127.0.0.1"]

# Set CSRF trusted origins
CSRF_TRUSTED_ORIGINS = (
    [f"https://{host}" for host in website_hostname.split(",")]
    if website_hostname
    else []
)

# Retrieve SITE_NAME
SITE_NAME = website_hostname

# Configure the default database
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": getenv("PGDATABASE"),
#         "USER": getenv("PGUSER"),
#         "PASSWORD": getenv("PGPASSWORD"),
#         "HOST": getenv("PGHOST"),
#         "PORT": getenv("PGPORT", 5432),
#         "OPTIONS": {
#             "sslmode": "require",
#             # "pool": {
#             #     "min_size": 2,
#             #     "max_size": 4,
#             #     "timeout": 10,
#             # },
#         },
#         "DISABLE_SERVER_SIDE_CURSORS": True,
#     }
# }

DATABASES = {
    "default": dj_database_url.config(
        default=os.getenv("DATABASE_URL"),
        conn_max_age=600,
        conn_health_checks=True,
    )
}


# Configure Cloudinary storage
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.getenv("CLOUDINARY_CLOUD_NAME"),
    "API_KEY": os.getenv("CLOUDINARY_API_KEY"),
    "API_SECRET": os.getenv("CLOUDINARY_API_SECRET"),
}

# Set media URL and default file storage
MEDIA_URL = "plantx/media/"
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
