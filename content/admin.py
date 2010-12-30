from django.contrib import admin
from EoSGP201011.content.models import Link, FlatPage, Partner

for cls in Link, FlatPage, Partner:
	admin.site.register(cls)
