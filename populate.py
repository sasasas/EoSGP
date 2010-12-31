#!/usr/bin/env python
from django.core.management import execute_manager
from django.core.management import setup_environ

try:
	import settings # Assumed to be in the same directory.
	setup_environ(settings)
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
	from content.models import FlatPage
	import glob
	PAGE_DIR = 'fixtures/static_pages/'
	filenames = glob.glob('%s*' % PAGE_DIR)
	for filename in filenames:
		permalink = filename.replace('.', '/').replace(PAGE_DIR, '')
		title = ' '.join([x.capitalize() for x in permalink.split('_')])
		page = FlatPage(permalink=permalink, title=title, content = open(filename).read())
		page.save()