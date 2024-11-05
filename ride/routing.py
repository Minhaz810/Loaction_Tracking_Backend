from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/driver-status/', consumers.DriverStatusConsumer.as_asgi()),
]