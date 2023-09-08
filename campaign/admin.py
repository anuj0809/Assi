from django.contrib import admin
from .models import Campaign, Subscriber

admin.site.register(Subscriber)
admin.site.register(Campaign)
