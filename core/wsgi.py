import os
from pathlib import Path

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR / ".env")

settings_module = (
    "core.settings.prod" if "WEBSITE_HOSTNAME" in os.environ else "core.settings.dev"
)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

application = get_wsgi_application()


# for vercel deployment
app = application
