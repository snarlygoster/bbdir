from django.contrib import admin
from joomlacontent.models import JosContent,JosSections,JosCategories
#from bookbinders.models import Image, Bookbinder

class JosContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'modified', 'state',)
    prepopulated_fields = { 'alias': ('title',)}


class JosCategoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'section', )



admin.site.register(JosCategories, JosCategoriesAdmin)
admin.site.register(JosContent, JosContentAdmin)

admin.site.register(JosSections)


# class ImageAdmin(admin.ModelAdmin):
#     date_hierarchy = 'upload_date'
#     list_display =('title', 'upload_date',)
#     save_as = True
#     save_on_top = True
# 
#  
# admin.site.register(Image, ImageAdmin)
# 
# 
# class BookbinderAdmin(admin.ModelAdmin):
# 
#     list_display = ('name','location','modified','created')
#     list_filter = ('modified',)
#     search_fields = ['name','location']
#  
#     filter_horizontal = ('image',)
#     readonly_fields = ('jostext','joscontent','joscreated')
#     save_as = True
#     save_on_top = True
#  
# admin.site.register(Bookbinder, BookbinderAdmin)