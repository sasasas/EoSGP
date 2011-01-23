from django.conf.urls.defaults import *
from django.views.generic import date_based
from django.views.generic.simple import direct_to_template
import os
from EoSGP201011 import views
from EoSGP201011.blog.models import Blog
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

archive_info = {
	'queryset': Blog.objects.all(),
	'date_field': 'datetime',
	'template_name': 'blog_archive.html',
	#'template_object_name': 'blog',
	#'allow_empty': 'False',
}

urlpatterns = patterns('',
    	(r'^(?:home/)?$', views.home),
	(r'^archive/$', date_based.archive_index, archive_info),
	(r'^about/$', views.about),
	(r'^partners/$', views.partners),
	(r'^about/aims_values/$', views.about),
	(r'^about/doctrinal_statement/$', views.doctrinal_statement),
	(r'^events/$', views.events),
	(r'^apprenticeships/$', views.apprenticeships),
	(r'^resources(?:/(?P<resource>\w+))?/$', views.resources),
	(r'^links/$', views.links),
	(r'^contact/$', views.contact),
	(r'^contact/thanks/$', direct_to_template, {'template' :'contact_thanks.html'}),
	(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        	{'document_root': os.path.join(os.path.dirname(__file__), 'static').replace('\\', '/')
}),
	#(r'^about/members/$', views.members),
	#(r'^blog_archive/$', views.blog_archive),
	

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
