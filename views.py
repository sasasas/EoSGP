from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import Context
from django.core.context_processors import csrf
from django.core.mail import mail_admins
from blog.models import Blog
from features.models import Event, BookOfTheMonth
from EoSGP201011.forms import ContactForm
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime

def home(request):
	next_event = Event.objects.filter(datetime__gte=datetime.now())[0]
	books_currentyear = BookOfTheMonth.objects.filter(date__year=datetime.now().year)	
	book_of_the_month = books_currentyear.get(date__month=datetime.now().month)
	latest_blog = Blog.objects.all()[0]
	return render_to_response('home.html', locals())

def about(request):
	t = get_template('about.html')
	html = t.render(Context())	
	return HttpResponse(html)

def doctrinal_statement(request):
	t = get_template('doctrinal_statement.html')
	html = t.render(Context())	
	return HttpResponse(html)

def events(request):
	event_list = Event.objects.filter(datetime__gte=datetime.now())	
	return render_to_response('events.html', {'event_list':event_list})

def contact(request):
	if request.method == 'POST':
		contact_form = ContactForm(request.POST)
		c = locals()
		c.update(csrf(request))
		if form.is_valid():
			cd = form.cleaned_data
			mail_admins(
				'Partnership info request: %s' % cd['church'],
				'You have received a request from %s at %s (minister: %s) for information on becoming a partner of EoSGP. E-mail: %s Address: %s Message: %s Newsletter: %s' % (cd['name'], cd['church'], cd['minister'], cd['email'], cd['address'], cd['message'], cd['newsletter']),
				fail_silently=False 
			)
			return HttpResponseRedirect('/contact/thanks')
		else:
			return render_to_response('contact.html', c)
	else:
		contact_form = ContactForm()
		c = locals()
		c.update(csrf(request))
		return render_to_response('contact.html', c)

def resources(request, resource):
	if resource in ['audio', 'video', 'literature']:
		filename = 'resources_%s.html' % resource
	else:
		filename = 'resources.html'
	t = get_template(filename)
	html = t.render(Context())	
	return HttpResponse(html)
	
