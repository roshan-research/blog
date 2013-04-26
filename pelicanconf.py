#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

script_path = os.path.realpath(__file__)
blog_base_path = os.path.dirname(script_path)

AUTHOR = u'سُبحه'
SITENAME = u'بلاگ سُبحه'
SITEURL = ''
THEME = 'theme'
PLUGIN_PATH = os.path.join(blog_base_path, 'plugins/')
PLUGINS = ['pelican-jalali']

TIMEZONE = 'Asia/Tehran'

DEFAULT_LANG = u'fa'
DATE_FORMATS = {'fa': '%d %B %Y'}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
