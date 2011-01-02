import os
import sys

paths = ['/home/ruby/EoSGP201011', '/home/ruby']
for path in paths:
  if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings_production'


import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

