from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from features.models import Event, BookOfTheMonth

def grab_latest_news(request):
	try:
		next_event = Event.objects.filter(datetime__gte=datetime.now())[0]
	except (ObjectDoesNotExist, IndexError):
		pass
	try:
		books_currentyear = BookOfTheMonth.objects.filter(date__year=datetime.now().year)	
		book_of_the_month = books_currentyear.get(date__month=datetime.now().month)
	except ObjectDoesNotExist:
		pass
	return locals()
