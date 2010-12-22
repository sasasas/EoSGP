from django.conf.urls.defaults import *
import os
from EoSGP201011 import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    	(r'^home/$', views.home),
	(r'^about/$', views.about),
	(r'^about/aims_values/$', views.about),
	(r'^about/doctrinal_statement/$', views.doctrinal_statement),
	(r'^events/$', views.events),
	(r'^contact/$', views.contact),
	(r'^resources/(?P<resource>\w+)?$', views.resources),
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
