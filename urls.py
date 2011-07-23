from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^abbm/', include('abbm.foo.urls')),
    url(r'^bbdir/', include('bbdir.urls')),
    
    # attachments application
    (r'^attachments/', include('attachments.urls')),
    
    # markitup application
    url(r'^markitup/', include('markitup.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
