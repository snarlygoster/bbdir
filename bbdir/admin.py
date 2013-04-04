from django.contrib import admin
from django.db import models

from attachments.admin import AttachmentInlines
from markitup.widgets import AdminMarkItUpWidget

from bbdir.models import Entry


class EntryAdmin(admin.ModelAdmin):
    inlines = [AttachmentInlines]
    formfield_overrides = {models.TextField: {'widget': AdminMarkItUpWidget}}
    list_display = ('name','city','state','modified','created','creator') 
    search_fields = [ 'name','city','state','creator__username' ]

admin.site.register(Entry,EntryAdmin)
