#!/usr/bin/python
##!/home/bookbind/django/bin/python
#/Library/WebServer/CGI-Executables/django/abbm/bin/python
# src: http://docs.python.org/howto/webservers.html#setting-up-fastcgi  
# setup the virtualenv
import os
os.environ.setdefault('PATH', '/bin:/usr/bin')
# os.environ['PATH'] = '/home/username/python/bin:' + os.environ['PATH']
# os.environ['VIRTUAL_ENV'] = '/home/username/python/bin'
# os.environ['PYTHON_EGG_CACHE'] = '/home/username/python/bin'


#os.environ['PATH'] = '/home/bookbind/django/bin/python/bin:' + os.environ['PATH']
#os.environ['VIRTUAL_ENV'] = '/home/bookbind/django/bin'
#os.environ['PYTHON_EGG_CACHE'] = '/home/bookbind/django/bin'

# os.chdir('/home/username/public_html/mezz')
os.chdir('/home/bookbind/django/')
import sys

# Add a custom Python path.
# sys.path.insert(0, "/home/username/public_html/")
sys.path.insert(0, "/home/bookbind/django/abbm/")
sys.path.insert(0, "/home/bookbind/django")

# Set the DJANGO_SETTINGS_MODULE environment variable  to the file in my
# application directory with the db settings etc.
# (filename minus the extension ".py")
os.environ['DJANGO_SETTINGS_MODULE'] = "abbm.settings"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
