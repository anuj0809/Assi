from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Subscriber, Campaign
from .email import send_email
import threading

def unsubscribe(request, email):
    subscriber = get_object_or_404(Subscriber, email=email)
    subscriber.active = False
    subscriber.save()
    return HttpResponse('You have been unsubscribed.')

def send_email_in_thread(subject, to, html):
    email_thread = threading.Thread(target=send_email, args=(subject, to, html))
    email_thread.start()

def send_campaign(campaign_id):
    campaign = Campaign.objects.get(id=campaign_id)
    subscribers = Subscriber.objects.filter(active=True)

    for subscriber in subscribers:
        html_content = render_to_string('campaign/campaign_email.html', {
            'subject': campaign.subject,
            'preview_text': campaign.preview_text,
            'article_url': campaign.article_url,
            'html_content': campaign.html_content
        })

        send_email_in_thread(campaign.subject, subscriber.email, html_content)

