from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.conf import settings
import hashlib
import hmac
from .models import Email

def verify_webhook(token, timestamp, signature):
    """Verify that the webhook request came from Mailgun"""
    signing_key = bytes(settings.MAILGUN_API_KEY, 'utf-8')
    verify_token = bytes(f'{timestamp}{token}', 'utf-8')
    
    hmac_digest = hmac.new(
        key=signing_key,
        msg=verify_token,
        digestmod=hashlib.sha256
    ).hexdigest()
    
    return hmac.compare_digest(signature, hmac_digest)

@csrf_exempt
def mailgun_webhook(request):
    if request.method != 'POST':
        return HttpResponse(status=405)
    
    # Verify webhook signature
    token = request.POST.get('token')
    timestamp = request.POST.get('timestamp')
    signature = request.POST.get('signature')
    
    if not verify_webhook(token, timestamp, signature):
        return HttpResponse(status=403)
    
    # Process the incoming email
    sender_email = request.POST.get('sender')
    recipient = request.POST.get('recipient')
    subject = request.POST.get('subject')
    body_plain = request.POST.get('body-plain')
    
    # Find the user associated with the recipient email
    try:
        user = User.objects.get(email=recipient)
    except User.DoesNotExist:
        return HttpResponse(status=200)  # Accept the webhook but don't process it
    
    # Create the email in our system
    Email.objects.create(
        subject=subject,
        body=body_plain,
        sender=user,  # The recipient becomes the "owner" in our system
        recipients=sender_email,
        direction='incoming',
        original_sender=sender_email,
    )
    
    return HttpResponse(status=200)