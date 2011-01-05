from django.contrib import admin
from features.models import LatestNewsShout, Event, BookOfTheMonth, Author

for cls in LatestNewsShout, Event, BookOfTheMonth, Author:
	admin.site.register(cls)

