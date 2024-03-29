import re
import os.path
import pdb
from urllib import unquote
from urlparse import urlparse
import imghdr

from markdown import markdown
from html2text import html2text
import BeautifulSoup

from django.utils.html import strip_tags
from django.template.defaultfilters import slugify
from django.core.files import File
from django.contrib.auth.models import User

from tagging.models import Tag
from joomlacontent.models import JosContent
from bbdir.models import Entry
from attachments.models import Attachment



# from django.utils.html import strip_tags
# from htmlentitydefs import name2codepoint
# 
# 
# def htmlentitydecode(s):
#     return re.sub('&(%s);' % '|'.join(name2codepoint), 
#             lambda m: unichr(name2codepoint[m.group(1)]), s)

JOOMLA_IMG_ROOT = '/home/bookbind/public_html/'

import_user = User.objects.get(username__exact='bookbind')

articles = JosContent.objects.using('joomla').filter(section__title='Bookbinders')
# bothtext = articles.exclude(introtext__exact='').exclude(fulltext__exact='')

def articles_to_binders(articles):
    for a in articles:
        articletobinder(a)
        
# m = re.match(r'(?P<name>[^(]*)\((?P<location>[^)]*)', title)
# l = re.match(r'(?P<city>\w*)\W*(?P<state>\w*).*$',  m.group('location'))

def articletobinder(article):
    bb = re.match(r'(?P<name>[^(]*)\(*(?P<location>[^)]*)', article.title)
    location_parts = bb.group('location').split(',')
    if len(location_parts) == 2 :
        (city, state) = location_parts
    else:
        city = bb.group('location').strip()
        state = ''
        
#   loc = re.match(r'(?P<city>\w*)\W*(?P<state>\w*).*$',  bb.group('location'))
#     if article.alias:
#         trimslug = re.match(r'[^\w]*([\w-]+)$', article.alias)
#         josslug = trimslug.group(1)
#     else:
#         josslug = slugify(bb.group('name').strip() + ' ' + bb.group('location').strip())
    
    jos_combined_text = article.introtext + article.fulltext
    entry = Entry.objects.create(
        name = bb.group('name').strip(),
        city = city.strip(),
        state = state.strip(),
        # location = bb.group('location').strip(),
        creator = import_user,
        )
    soup = BeautifulSoup.BeautifulSoup(jos_combined_text)
    for img in soup.findAll('img', src=True):
        absolutepath = os.path.join(JOOMLA_IMG_ROOT, unquote(img['src']))
        os.chdir(os.path.dirname(absolutepath))
        try:
            pict = File(open(os.path.basename(absolutepath), 'r'))
            a = Attachment()
            a.creator = import_user
            a.content_object = entry
            a.attachment_file = pict
            a.save()
            pict.close()
            img['src'] = urlparse(a.attachment_file.url)[2] # python 2.4 version 
                                                            # of urlparse
        except IOError:
            print 'cannot open ' , absolutepath
    
    entry.content = html2text(unicode(soup))
    entry.save()
    Tag.objects.add_tag(entry, 'joomlacontent')
#     binder, newly_created = Bookbinder.objects.get_or_create(
#         joscontent = article, 
#         name = bb.group('name').strip(), 
#         location = bb.group('location').strip(), 
#         joscreated = article.created, 
#         jostext = jos_combined_text,
#         slug = josslug,
#         )
#     imgs = import_images(jos_combined_text)
#     for img in imgs:
#         if img:
#             binder.image.add(img)
#     
    
def create_image_from_path(path):
    
    try:
        image_type = imghdr.what(path)
        if not image_type:
            raise IOError("not image type")
        f = ImageFile(open(path))
        image, newly_created = Image.objects.get_or_create(
            img = f,
            title = os.path.basename(f.name),
            height = f.height,
            width = f.width,
            credit = 'Joomla Import',)
        return image
    except IOError:
        print 'IOError: could not open %s' % path
    

# print htmlentitydecode(strip_tags(articles[2].introtext))
# print markdown(htmlentitydecode(strip_tags(articles[2].introtext)))