# Create your views here.
from django.views.generic import DetailView, ListView

from bbdir.models import Entry
from namepaginator.chunkpaginator import ChunkPaginator

def create_namepaginator(request, object_list, on='name', per_page = 10):
    
    paginator = NamePaginator(object_list, on = on, per_page = per_page)
    
    print on
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        page = paginator.page(page)
    except (InvalidPage):
        page = paginator.page(paginator.num_pages)
    return page


class BinderDirectoryListView(ListView):
    """
class PublisherDetailView(DetailView):

    context_object_name = "publisher"
    model = Publisher

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PublisherDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Book.objects.all()
        return context
        
    """
    model = Entry
    per_page = 10
    paginator_class = ChunkPaginator
    paginate_by = 20
    
    def get_queryset(self):
        self.on = self.kwargs['sort_by']
        
        
        return Entry.objects.order_by(self.on)
        
        
    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return ChunkPaginator(queryset, per_page, orphans, allow_empty_first_page, on=self.on)

#     def get_context_data(self, **kwargs):
#         context = super(BinderDirectoryListView, self).get_context_data(**kwargs)
#         print 'Here'
#         context['page'] = create_namepaginator(self.request, self.object_list, on='name', per_page = self.per_page)
#         return context
        

class BinderDirectoryDetailView(DetailView):
    model=Entry

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BinderDirectoryDetailView, self).get_context_data(**kwargs)
        context['sort_by'] = self.kwargs['sort_by']
        context['slug'] = self.kwargs['slug']
        context['path_info'] = self.request.path_info
        context['path'] = self.request.get_full_path()
        context['up_path'] = context['path'].replace(context['slug'] + '/', '')
        
        return context