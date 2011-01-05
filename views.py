from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import  Context, RequestContext, TemplateDoesNotExist
from django.core.mail import mail_admins
from django.core.exceptions import ObjectDoesNotExist
from blog.models import Blog
from features.models import LatestNewsShout, Event, BookOfTheMonth
from content.models import Link, Partner, FlatPage
from forms import ContactForm
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
	page = get_object_or_404( FlatPage, permalink=permalink)
	try:
		template = get_template(page.template_file)
	except TemplateDoesNotExist:
		template = get_template("flat_page.html")
	return HttpResponse(template.render(RequestContext(request, {'page':page})))

def partners(request):
	try:
		page = FlatPage.objects.get(permalink='partners')
	except ObjectDoesNotExist:
		page = FlatPage()
	partner_list = Partner.objects.all()
	return render_to_response('partners.html', locals(), context_instance=RequestContext(request))

def events(request):
	try:
		page = FlatPage.objects.get(permalink='events')
	except ObjectDoesNotExist:
		page = FlatPage(permalink = 'events', title = 'Events')
	event_list = Event.objects.filter(datetime__gte=datetime.now())	
	return render_to_response('events.html', {'event_list':event_list}, context_instance=RequestContext(request))

def resources(request, resource):
	if resource in ['audio', 'video', 'literature']:
		filename = 'resources_%s.html' % resource
	else:
		filename = 'resources.html'
	return render_to_response(filename, {}, context_instance=RequestContext(request))

def links(request):
	try:
		page = FlatPage.objects.get(permalink='links')
	except ObjectDoesNotExist:
		page = FlatPage(permalink = 'links', title = 'Links')
	return render_to_response('links.html', locals(), context_instance=RequestContext(request))

def contact(request):
	try:
		page = FlatPage.objects.get(permalink='contact')
	except ObjectDoesNotExist:
		page = FlatPage(permalink = 'contact', title = 'Contact')
	if request.method == 'POST':
		contact_form = ContactForm(request.POST)
		if contact_form.is_valid():
			cd = contact_form.cleaned_data
			email_template = get_template('email/contact.email')
			email_body = email_template.render(Context(cd))
			mail_admins(
				'Partnership info request: %s' % cd['church_or_org'],
				 email_body),
				fail_silently=False 
			)
			return HttpResponseRedirect('/contact/thanks')
		else:
			return render_to_response('contact.html', {'contact_form':contact_form, 'page':page}, context_instance=RequestContext(request))
	else:
		contact_form = ContactForm()
		return render_to_response('contact.html', {'contact_form':contact_form, 'page':page}, context_instance=RequestContext(request))
