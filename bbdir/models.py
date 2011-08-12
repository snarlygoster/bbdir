from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django_extensions.db.fields import  AutoSlugField
                                         
from django.template.defaultfilters import slugify

# Create your models here.
from bbdir.mdsyntax import markdown_syntax_summary # help text

class Entry(models.Model):
    """Entry"""
    name = models.CharField( max_length=255, blank=False, null=True, help_text="enter as 'Lastname, Firstname' or Business Name")
    #location = models.CharField( max_length=300, blank=True, null=True, help_text="legacy joomla location format")
    city = models.CharField( max_length=255, blank=True, null=True,)
    state = models.CharField( max_length=3, blank=True, null=True, help_text="two letter postal abbreviation")
    
    slug = AutoSlugField(populate_from = ['name', 'location'])
    
    content = models.TextField(blank=True, help_text = markdown_syntax_summary )
    
    modified = models.DateTimeField( blank=True, null=True, auto_now=True)
    created = models.DateTimeField( blank=True, null=True, auto_now_add=True)
    
    creator = models.ForeignKey(User)
    
    def _get_location(self):
        if self.city and self.state:
            location =  "%s, %s" % (self.city,self.state)
        elif self.city and not self.state:
            location =  self.city
        elif self.state and not self.city:
            location =  self.state
        else:
            location =  ''
        return location

    location = property(_get_location)
    
    class Meta:
        ordering = ['name', 'city', 'state']
        verbose_name_plural = "Entries"
 
    def __unicode__(self):
        return "%s - %s" % (self.name, self.location)
 
    @models.permalink
    def get_absolute_url(self):
        return ('entry-detail', ([self.slug]))
