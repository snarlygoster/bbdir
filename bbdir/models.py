from django.db import models

# Create your models here.
from django_extensions.db.fields import  AutoSlugField
                                         
from django.template.defaultfilters import slugify

# Create your models here.
from bbdir.mdsyntax import markdown_syntax_summary

class Entry(models.Model):
    """Entry"""
    name = models.CharField( max_length=255, blank=False, null=True, help_text="enter as 'Lastname, Firstname' or Business Name")
    city = models.CharField( max_length=255, blank=True, null=True,)
    state = models.CharField( max_length=3, blank=True, null=True, help_text="two letter postal abbreviation")
    
    slug = AutoSlugField(populate_from = ['name', 'city', 'state'])
    
    content = models.TextField(blank=True,
    help_text = markdown_syntax_summary )

    class Meta:
        ordering = ['name', 'city', 'state']
 
    def __unicode__(self):
        return "%s - %s, %s" % (self.name, self.city, self.state)
 
    @models.permalink
    def get_absolute_url(self):
        return ('entry-detail', ([self.slug]))
