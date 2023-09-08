from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

def send_email(subject, to_email, html_content):
    text_content = strip_tags(html_content)  # This will extract plain text from HTML content
    email = EmailMultiAlternatives(
        subject,
        text_content,
        '<your-email-address>',
        [to_email]
    )
    email.attach_alternative(html_content, "text/html")
    email.send()
