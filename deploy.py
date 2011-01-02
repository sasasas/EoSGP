import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'EoSGP201011.settings_production'

path = '/home/ruby/EoSGP201011'
if path not in sys.path:
    sys.path.append(path)

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

