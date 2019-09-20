from django.urls import path

from .consumers import ReleaseConsumer

websocket_urlpatterns = [
    path('ws/release/', ReleaseConsumer),
]
