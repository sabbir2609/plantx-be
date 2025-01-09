from django.db import models
from users.models import User

class Email(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    sender = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='sent_emails'
    )
    recipients = models.CharField(max_length=500)  # Store as comma-separated emails
    cc = models.CharField(max_length=500, blank=True)
    bcc = models.CharField(max_length=500, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_draft = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.subject} - {self.sender.email}"
