from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
import os
import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^(?:home/)?$', views.home),
#	(r'^resources(?:/(?P<resource>\w+))?/$', views.resources),
	(r'^events/$', views.events),
	(r'^partners/$', views.partners),
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
