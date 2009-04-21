#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import sys

import cherrypy

from controllers import *

def start():
    appconf = {
                '/': {
                        'tools.proxy.on':True,
                     }
              }

    cherrypy.config.update({
                            'server.socket_port':8087
                            })

    cherrypy.quickstart(IndexController(), '/', appconf)
    
    return 0

if __name__ == '__main__':
    sys.exit(start())


