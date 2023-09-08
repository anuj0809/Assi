from django.urls import path
from .views import unsubscribe

urlpatterns = [
    path('unsubscribe/<str:email>/', unsubscribe, name='unsubscribe'),
]
