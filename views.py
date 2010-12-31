from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import  Context, RequestContext, TemplateDoesNotExist
from django.core.mail import mail_admins
from django.core.exceptions import ObjectDoesNotExist
from blog.models import Blog
from features.models import LatestNewsShout, Event, BookOfTheMonth
from content.models import Link, Partner, FlatPage
from EoSGP201011.forms import ContactForm
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.simple import direct_to_template
from datetime import datetime
from django.shortcuts import get_object_or_404

def home(request):
	try:
		latest_blog = Blog.objects.all()[0]
	except (ObjectDoesNotExist, IndexError):
		pass
	return render_to_response('home.html', locals(), context_instance=RequestContext(request))

def flatpage(request, permalink):
	page = get_object_or_404(FlatPage, permalink=permalink)
	try:
		template = get_template("%s.html" % permalink)
	except TemplateDoesNotExist:
		template = get_template("flat_page.html")
	return HttpResponse(template.render(RequestContext(request, {'page':page})))

def partners(request):
	page = FlatPage.objects.get(permalink='partners')
	partner_list = Partner.objects.all()
	return render_to_response('partners.html', locals(), context_instance=RequestContext(request))

def events(request):
	event_list = Event.objects.filter(datetime__gte=datetime.now())	
	return render_to_response('events.html', {'event_list':event_list}, context_instance=RequestContext(request))

def resources(request, resource):
	if resource in ['audio', 'video', 'literature']:
		filename = 'resources_%s.html' % resource
	else:
		filename = 'resources.html'
	return render_to_response(filename, {}, context_instance=RequestContext(request))

def links(request):
	return render_to_response('links.html', locals(), context_instance=RequestContext(request))

def contact(request):
	if request.method == 'POST':
		contact_form = ContactForm(request.POST)
		if contact_form.is_valid():
			email_body = '''
You have received a request from %s at %s (minister: %s) for information on becoming a partner of EoSGP (%s). 

E-mail: %s 

Address: %s 

Message: %s 

Newsletter: %s
'''
			cd = contact_form.cleaned_data
			mail_admins(
				'Partnership info request: %s' % cd['church_or_org'],
				 email_body % (cd['name'], cd['church_or_org'], cd['minister_or_head'], cd['org_type'], cd['email'], cd['address'], cd['message'], cd['newsletter']),
				fail_silently=False 
			)
			return HttpResponseRedirect('/contact/thanks')
		else:
			return render_to_response('contact.html', {'contact_form':contact_form}, context_instance=RequestContext(request))
	else:
		contact_form = ContactForm()
		return render_to_response('contact.html', {'contact_form':contact_form}, context_instance=RequestContext(request))


	
