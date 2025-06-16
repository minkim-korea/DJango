
import os
from channels.routing import ProtocolTypeRouter 
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE' ,'<project이름>.settings')

application = ProtocolTypeRouter ({ 
    'http':get_asgi_application()
})
