import requests
from django.conf import settings

def send_email_mailgun(email_obj):
    """
    Send email using Mailgun API
    """
    MAILGUN_DOMAIN = "theviriditas.com"
    MAILGUN_API_KEY = settings.MAILGUN_API_KEY
    
    return requests.post(
        f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
        auth=("api", MAILGUN_API_KEY),
        data={
            "from": f"{email_obj.sender.get_full_name()} <{email_obj.sender.email}>",
            "to": email_obj.recipients,
            "cc": email_obj.cc,
            "bcc": email_obj.bcc,
            "subject": email_obj.subject,
            "text": email_obj.body
        }
    )