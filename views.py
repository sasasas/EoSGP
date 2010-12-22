from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import Context, RequestContext
from django.core.context_processors import csrf
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import mail_admins
from blog.models import Blog
from features.models import Event, BookOfTheMonth
from EoSGP201011.forms import ContactForm
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime

def home(request):
	latest_blog = Blog.objects.all()[0]
	return render_to_response('home.html', locals(), context_instance=RequestContext(request))

def about(request):
	return render_to_response('about.html', locals(), context_instance=RequestContext(request))

def doctrinal_statement(request):
	return render_to_response('doctrinal_statement.html', locals(), context_instance=RequestContext(request))

def partners(request):
	return render_to_response('partners.html', locals(), context_instance=RequestContext(request))

def events(request):
	event_list = Event.objects.filter(datetime__gte=datetime.now())	
	return render_to_response('events.html', {'event_list':event_list}, context_instance=RequestContext(request))

def apprenticeships(request):
	return render_to_response('apprenticeships.html', locals(), context_instance=RequestContext(request))

def resources(request, resource):
	if resource in ['audio', 'video', 'literature']:
		filename = 'resources_%s.html' % resource
	else:
		filename = 'resources.html'
	t = get_template(filename)
	html = t.render(Context())	
	return HttpResponse(html)

def links(request):
	return render_to_response('links.html', locals(), context_instance=RequestContext(request))

def contact(request):
	if request.method == 'POST':
		contact_form = ContactForm(request.POST)
		c = locals()
		c.update(csrf(request))
		if contact_form.is_valid():
			cd = contact_form.cleaned_data
			mail_admins(
				'Partnership info request: %s' % cd['church_or_org'],
				'You have received a request from %s at %s (minister: %s) for information on becoming a partner of EoSGP (%s). E-mail: %s Address: %s Message: %s Newsletter: %s' % (cd['name'], cd['church_or_org'], cd['minister_or_head'], cd['org_type'], cd['email'], cd['address'], cd['message'], cd['newsletter']),
				fail_silently=False 
			)
			return HttpResponseRedirect('/contact/thanks')
		else:
			return render_to_response('contact.html', c, context_instance=RequestContext(request))
	else:
		contact_form = ContactForm()
		c = locals()
		c.update(csrf(request))
		return render_to_response('contact.html', c, context_instance=RequestContext(request))


	
