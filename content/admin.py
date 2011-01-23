from django.contrib import admin
from content.models import Link, FlatPage, Partner

for cls in Link, FlatPage, Partner:
	admin.site.register(cls)
