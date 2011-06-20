from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djproj.views.home', name='home'),
    # url(r'^djproj/', include('djproj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
url(r'^', include('cms.urls')),
)

#if settings.DEBUG:
#	urlpatterns += patterns('',
#		(r'^' + settings.MEDIA_URL.lstrip('/'), include('appmedia.urls')),
#	) + urlpatterns

urlpatterns += staticfiles_urlpatterns()
#assert False
