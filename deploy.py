import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

path = '/home/ruby/EoSGP201011'
if path not in sys.path:
    sys.path.append(path)

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

