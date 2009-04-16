#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import sys

import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        yield "The current time is %s<br />" % time.ctime()
        yield "A <a href='static/test.txt'>static file</a> served by Apache."

def start():
    appconf = {
                '/': {
                        'tools.proxy.on':True,
                     }
              }

    cherrypy.config.update({
                            'server.socket_port':8087
                            })

    cherrypy.quickstart(HelloWorld(), '/', appconf)
    
    return 0

if __name__ == '__main__':
    sys.exit(start())


