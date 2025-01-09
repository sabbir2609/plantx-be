from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Email
from .utils import send_email_mailgun

@receiver(post_save, sender=Email)
def send_email(sender, instance, created, **kwargs):
    if created and not instance.is_draft:
        send_email_mailgun(instance)