from django.conf.urls import url

from . import consumers

websock_urlpatterns = [
    url(r'^ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatConsumer)
]