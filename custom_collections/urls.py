#from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
import os

urlpatterns = patterns('',
    url(r'^jstree/', 'custom_collections.views.collections_jstree'),
    url(r'^$', 'custom_collections.views.collections')
)