import os
import sys

#Paths of the CWD and its parent are added to the PYTHONPATH
paths = [os.path.dirname(__file__), os.path.dirname(os.path.dirname(__file__))]
for path in paths:
  if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings_production'


import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

