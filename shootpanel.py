#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
from tornado import template
import tornado.httpclient
import os
import pymongo
import re
import zlib
import json
import yaml

try:
    connection = pymongo.MongoClient("localhost", 27017) 
    db = connection.b2b
except Exception:
    db = None
#from qabs.common.yabs_utils import prepare_http_request
#from qabs.common.cannon import Cannon


class ShootHandler(tornado.web.RequestHandler):
    def post(self):
        print "khjghj"
        print self.get_argument('shootCount', '')
        print self.get_argument('isDebug', '')
        print self.get_argument('isPageCode', '')



class MongoHandler(tornado.web.RequestHandler):
    def get(self):
        self.write({'response_log': db.response_log.count() if db else -1, 'http_diff': db.http_diff.count() if db else -1})

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            try:
                with open("set.conf", 'r') as f:
                    last_config = {}
                    last_config = yaml.load(f)
                    last_config['status'] = 'Предыдущий конфиг найден, значения загружены'
            except EnvironmentError: # parent of IOError, OSError *and* WindowsError where available   
                last_config = {'status': 'Предыдущий конфиг отсутствует, текущие настройки сохранятся в момент отстрела'}
            self.render("main.html", last_config=last_config, resp_count=db.response_log.count() if db else -1, 
                http_count=db.http_diff.count() if db else -1)

        except Exception as e:
            print e

class CrossCheckHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            self.render("cc.html")
        except Exception as e:
            print e

class NewLogsHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            self.render("newlog.html")
        except Exception as e:
            print e

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/b2b", MainHandler),
            (r"/cc", CrossCheckHandler),
            (r"/newlog", NewLogsHandler),
            (r"/mongo_count", MongoHandler),
            (r"/run", ShootHandler),

            # Add more paths here
        ]
        settings = {
            "debug": True,
            "template_path": os.path.join(os.path.dirname(__file__), "tpl"),
            "static_path": os.path.join(os.path.dirname(__file__),"static")
        }
        tornado.web.Application.__init__(self, handlers, **settings)


application = Application() 

if __name__ == "__main__":
        application.listen(8888)
        tornado.ioloop.IOLoop.instance().start()
