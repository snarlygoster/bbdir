from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class JosSections(models.Model):
    # id = models.IntegerField(primary_key=True)
    # title = models.CharField(max_length=765)
    # name = models.CharField(max_length=765)
    # alias = models.CharField(max_length=765)
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    image = models.TextField()
    # scope = models.CharField(max_length=150)
    scope = models.CharField(max_length=50)
    # image_position = models.CharField(max_length=90)
    image_position = models.CharField(max_length=30)
    description = models.TextField()
    published = models.IntegerField()
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    ordering = models.IntegerField()
    access = models.IntegerField()
    count = models.IntegerField()
    params = models.TextField()
    class Meta:
        db_table = u'jos_sections'
        verbose_name, verbose_name_plural = "JosSection", "JosSections"
    def __unicode__(self):
        return self.title

class JosCategories(models.Model):
    # id = models.IntegerField(primary_key=True)
    # parent_id = models.IntegerField()
    parent = models.ForeignKey('self', db_column='parent_id', default=0)
    # title = models.CharField(max_length=765)
    # name = models.CharField(max_length=765)
    # alias = models.CharField(max_length=765)
    # image = models.CharField(max_length=765)
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    # alias = models.CharField(max_length=255)
    alias = models.SlugField(max_length=255)
    image = models.CharField(max_length=255)
    # section = models.CharField(max_length=150)
    section = models.CharField(max_length=50)
    # image_position = models.CharField(max_length=90)
    image_position = models.CharField(max_length=30)
    description = models.TextField()
    published = models.IntegerField()
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    # editor = models.CharField(max_length=150, blank=True)
    editor = models.CharField(max_length=50, blank=True)
    ordering = models.IntegerField()
    access = models.IntegerField()
    count = models.IntegerField()
    params = models.TextField()
    class Meta:
        db_table = u'jos_categories'
        verbose_name, verbose_name_plural = 'JosCategory', 'JosCategories'
    def __unicode__(self):
        return self.title

class JosContentRating(models.Model):
    content_id = models.IntegerField(primary_key=True)
    rating_sum = models.IntegerField()
    rating_count = models.IntegerField()
    lastip = models.CharField(max_length=150)
    class Meta:
        db_table = u'jos_content_rating'

class JosContent(models.Model):
    # id = models.IntegerField(primary_key=True)
    # title = models.CharField(max_length=765)
    # alias = models.CharField(max_length=765)
    # title_alias = models.CharField(max_length=765)
    title = models.CharField(max_length=255)
    # alias = models.CharField(max_length=255)
    alias = models.SlugField(max_length=255)
    title_alias = models.CharField(max_length=255)
    introtext = models.TextField()
    fulltext = models.TextField()
    state = models.IntegerField()
    # sectionid = models.IntegerField()
    section = models.ForeignKey(JosSections, db_column='sectionid')
    mask = models.IntegerField()
    # catid = models.IntegerField()
    cat = models.ForeignKey(JosCategories, db_column='catid', default=0)
    created = models.DateTimeField()
    # created_by = models.IntegerField()
    created_by = models.ForeignKey(User, db_column='created_by')
    modified = models.DateTimeField()
    modified_by = models.IntegerField()
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()
    publish_up = models.DateTimeField()
    publish_down = models.DateTimeField()
    images = models.TextField()
    urls = models.TextField()
    attribs = models.TextField()
    version = models.IntegerField()
    parentid = models.IntegerField()
    ordering = models.IntegerField()
    metakey = models.TextField()
    metadesc = models.TextField()
    # access = models.IntegerField()
    access = models.ForeignKey(JosContentRating, to_field='content_id', db_column='access')
    hits = models.IntegerField()
    metadata = models.TextField()
    class Meta:
        db_table = u'jos_content'
        verbose_name, verbose_name_plural="JosArticle", "JosArticles"
    def __unicode__(self):
        return self.title
    
# class JosContentFrontpage(models.Model):
#     # content_id = models.ForeignKey(JosContent, primary_key=True)
#     content = models.ForeignKey(JosContent, primary_key=True, db_column='content_id')
#     ordering = models.IntegerField()
#     class Meta:
#         db_table = u'jos_content_frontpage'


