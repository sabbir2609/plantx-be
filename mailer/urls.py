from django.urls import path
from .views import mailgun_webhook


app_name = "mailer"

urlpatterns = [
    path("mailgun/", mailgun_webhook, name="mailgun_webhook"),
]