#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from os.path import dirname, abspath, join
root_path = abspath(dirname(__file__))
sys.path.insert(0, root_path)

import cherrypy
from genshi.core import Stream
from genshi.output import encode, get_serializer
from genshi.template import Context, TemplateLoader
from genshi.filters import HTMLFormFiller

template_path = join(root_path, 'templates')
loader = TemplateLoader(
    template_path,
    auto_reload=True
)

class IndexController(object):
    @cherrypy.expose
    def index(self):
        tmpl = loader.load('index.html')
        return tmpl.generate().render('html', doctype='html')
