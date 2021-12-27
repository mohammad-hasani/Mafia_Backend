from django.urls import re_path
from . import consumers


websocket_urlpattern = [
    re_path(r'ws/game/admin', consumers.GameConsumerAdmin.as_asgi()),
    re_path(r'ws/game/user', consumers.GameConsumerUser.as_asgi()),
]