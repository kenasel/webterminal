from django.urls import path, re_path

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from .consumers import MyConsumer, MyAsyncConsumer


application = ProtocolTypeRouter({

    # WebSocket handler
    "websocket": 
        URLRouter([
            re_path(r"^terminals/(?P<hosts>.*)/(?P<port>.*)/(?P<username>.*)/(?P<password>.*)/$", MyConsumer),
        ])
    ,
})