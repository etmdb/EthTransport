"""
Ethiopian Transport API
WSGI config for guzo project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

__author__ = "Dawit Nida (dchonch@gmail.com)"
__date__ = "Date: 18/11/2017"
__version__ = "Version: 1.0.0"
__Copyright__ = "Copyright: @dawitnida"

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "guzo.settings")

application = get_wsgi_application()
