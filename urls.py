from django.conf.urls.defaults import *
from django.views.generic import date_based
from django.views.generic.simple import direct_to_template
import os
import views
from blog.models import Blog
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

archive_info = {
	'queryset': Blog.objects.all(),
	'date_field': 'datetime',
	'template_name': 'blog_archive.html',
	'template_object_name': 'blogs',
	'num_latest': False
}

archive_year = {
	'queryset': Blog.objects.all(),
	'date_field': 'datetime',
	'template_name': 'blog_archive_year.html',
	'make_object_list': True,

}



urlpatterns = patterns('',
    	(r'^(?:home/)?$', views.home),
	(r'^events/$', views.events),
	(r'^partners/$', views.partners),
	(r'^archive/$', date_based.archive_index, archive_info),
	(r'^archive/(?P<year>20\d\d)/$', date_based.archive_year, archive_year),
	(r'^links/$', views.links),
	(r'^contact/$', views.contact),
	(r'^contact/thanks/$', direct_to_template, {'template' :'contact_thanks.html'}),
	(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        	{'document_root': os.path.join(os.path.dirname(__file__), 'static').replace('\\', '/')
}),
	(r'^uploaded_graphics/(?P<path>.*)$', 'django.views.static.serve',
        	{'document_root': os.path.join(os.path.dirname(__file__), 'uploaded_graphics').replace('\\', '/')
}),
	#(r'^about/members/$', views.members),
	#(r'^blog_archive/$', views.blog_archive),
	

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    # Catchall for the semi-static pages. Will give confusing errors for 404 though, so be careful!
	(r'^(?P<permalink>.*)/$', views.flatpage),
)
