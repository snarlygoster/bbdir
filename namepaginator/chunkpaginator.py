#
from django.core.paginator import Paginator

#class Paginator(object_list, per_page, orphans=0, allow_empty_first_page=True)

class ChunkPaginator(Paginator):
    def __init__(self, object_list, per_page, orphans=0, allow_empty_first_page=True,on=None):
        self.on=on
        super(ChunkPaginator, self).__init__(object_list, per_page, orphans=0, allow_empty_first_page=True)
    def _get_chunks(self):
        chunks = []
        page_num = 1
        object_sum = 0
    #   initials = [n[0][0] if len(n[0]) else u'' for n in self.object_list.values_list(self.on)]
        initials = [ (len(n[0]) and [n[0][0]] or [u''])[0]     for n in self.object_list.values_list(self.on)]
        for letter in sorted(set(initials)):
            chunks.append({'key': letter, 'page_num': page_num})
            object_sum += initials.count(letter)
            page_num = object_sum/self.per_page+1
        self.is_chunkinated = len(chunks) > 1
        return chunks
    chunks = property(_get_chunks)
