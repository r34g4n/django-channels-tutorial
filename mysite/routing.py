from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import chat.routing

application = ProtocolTypeRouter({
    # (http-> django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websockets_urlpatterns
        )
    )
})