import os

from django.core.wsgi import get_wsgi_application

settings_module = (
    "core.settings.prod" if "WEBSITE_HOSTNAME" in os.environ else "core.settings.dev"
)

print(f"Using settings module: {settings_module}")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

application = get_wsgi_application()


# for vercel deployment
app = application
