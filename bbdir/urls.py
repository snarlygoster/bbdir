from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView, UpdateView, CreateView

from bbdir.models import Entry

urlpatterns = patterns('', 
    (r'^$', ListView.as_view(model = Entry)),
    url(r'^(?P<slug>[\w-]+)/$', DetailView.as_view(model=Entry,), name = 'entry-detail' ),
    url(r'^(?P<slug>[\w-]+)/edit/$', UpdateView.as_view(model=Entry,), name = 'entry-edit' ),
   
)