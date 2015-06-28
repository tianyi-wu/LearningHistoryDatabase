"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import site
import sys

site.addsitedir("/usr/local/bin")

sys.path.append('/~learning/learning /home/learning/learning_system/mysite')
sys.path.append('/~learning/learning /home/learning/learning_system/mysite/mysite')



os.environ["DJANGO_SETTINGS_MODULE"] = "mysite.settings"



activate_env = os.path.expanduser("/home/learning/LEARNING/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
