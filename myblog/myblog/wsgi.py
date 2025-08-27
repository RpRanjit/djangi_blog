"""
WSGI config for myblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys

# Add your project directory to the Python path
path = '/home/your_username/djangi_blog/myblog'
if path not in sys.path:
    sys.path.append(path)

# Set environment variables
os.environ['DJANGO_SETTINGS_MODULE'] = 'myblog.settings'
os.environ['SECRET_KEY'] = 'django-insecure-wd+@hagdvwy0634&)%uto$!cw#7_duib&9-$&wjp#iu2^v$4^4'
os.environ['EMAIL_HOST_USER'] = '98160rp@gmail.com'
os.environ['EMAIL_HOST_PASSWORD'] = 'tbqa drkm cbrh klgk'

# Import and run Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()