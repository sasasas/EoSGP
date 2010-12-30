from django.contrib import admin
from EoSGP201011.features.models import LatestNewsShout, Event, BookOfTheMonth, Author

for cls in LatestNewsShout, Event, BookOfTheMonth, Author:
	admin.site.register(cls)

