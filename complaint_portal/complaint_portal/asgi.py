"""
ASGI config for complaint_portal project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application #is a Django function that creates an ASGI-compatible application instance.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'complaint_portal.settings')#sets the evironment to use file

application = get_asgi_application()#This initializes the Django ASGI application
#created django applicaton  