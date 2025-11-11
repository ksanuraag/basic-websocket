from django.urls import re_path

import chat.consumers

websocket_urls=[
    re_path(r'ws/chat/$',chat.consumers.ChatConsumer.as_asgi())
]