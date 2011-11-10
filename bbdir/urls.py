from django.conf.urls.defaults import *
#from django.views.generic import DetailView, ListView, UpdateView, CreateView

from bbdir.views import BinderDirectoryListView, BinderDirectoryDetailView


urlpatterns = patterns('', 
    url(r'^(?P<sort_by>[\w]+)/$', BinderDirectoryListView.as_view(), name='entry-list'),
    url(r'^(?P<sort_by>[\w]+)/(?P<slug>[\w-]+)/$', BinderDirectoryDetailView.as_view(), name = 'entry-detail' ),
    url(r'^/$', BinderDirectoryListView.as_view(), name='entry-list-root'),

)