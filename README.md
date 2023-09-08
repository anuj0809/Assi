# Email Campaign Manager

Email Campaign Manager is a Django web application that allows users to create and manage email campaigns. The application supports adding subscribers, creating campaigns, and sending emails to active subscribers. The emails are sent using SMTP and the content of the emails is rendered from a base template.

## Features

- Subscriber management (Add, Unsubscribe)
- Email campaign creation and management
- Sending email campaigns to active subscribers using SMTP
- Optimize the sending time by using Python's threading for dispatching emails in parallel
- An HTML page for managing campaigns and subscribers

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

To run this project, you will need:

- Python 3.7 or later
- Django 2.2 or later
- A Mailgun account and sandbox

### Installation

1. Clone the repository

2. Install the dependencies

   ```
   pip install -r requirements.txt
   ```

3. Set up your Mailgun credentials in settings.py:

   ```python
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'smtp.mailgun.org'
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_HOST_USER = '<your-mailgun-smtp-username>'
   EMAIL_HOST_PASSWORD = '<your-mailgun-smtp-password>'
   DEFAULT_FROM_EMAIL = '<your-email-address>'
   ```

4. Run the migrations:

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start the Django server:
   ```
   python manage.py runserver
   ```

### How to Run

1. Go to terminal and run this:

```python
python manage.py shell
```

2. Then, in the shell:

```python
from campaign.views import send_campaign
send_campaign(campaign_id)
```

Replace campaign_id with the ID of the campaign you want to send.

### Unsubscribe a User

To unsubscribe a user, navigate to http://127.0.0.1:8000/unsubscribe/email, replacing email with the email address of the subscriber you want to unsubscribe.

### Usage

1. Navigate to the Django admin panel (usually http://127.0.0.1:8000/admin) and log in.

2. Go to the Campaigns section and click on "Add Campaign" to create a new email campaign.

3. Fill in the required details such as the subject, preview text, article URL, HTML content, and plain text content, and save the campaign.

4. To send the campaign, select the campaign(s) from the list and choose the "Run selected campaigns" action.
