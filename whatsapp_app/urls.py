from django.urls import path
from .views import send_message_view, whatsapp_webhook

urlpatterns = [
    path('send-message/', send_message_view, name='send_message'),
    path('webhook/', whatsapp_webhook, name='webhook'),
]
