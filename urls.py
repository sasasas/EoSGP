from django.conf.urls.defaults import *
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
	(r'^resources/$', views.resources),
	(r'^resources/audio/$', views.resources_audio),
	(r'^resources/video/$', views.resources_video),
	(r'^resources/literature/$', views.resources_literature),
	(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        	{'document_root': '/home/sasasas/webwork/EoSGP201011/static'}),
	#(r'^about/members/$', views.members),
	#(r'^blog_archive/$', views.blog_archive),
	

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
