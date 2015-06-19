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

connection = pymongo.MongoClient("localhost", 27017) 
db = connection.b2b
#from qabs.common.yabs_utils import prepare_http_request
#from qabs.common.cannon import Cannon


class MongoHandler(tornado.web.RequestHandler):
    def get(self):
        self.write({'response_log': db.response_log.count(), 'http_diff': db.http_diff.count()})

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        try:
            try:
                with open("last.config", 'r') as f:
                    last_config = yaml.load(f)
                    last_config['status'] = 'Предыдущий конфиг найден, использовались значения:'
            except EnvironmentError: # parent of IOError, OSError *and* WindowsError where available   
                last_config = {'status': 'Предыдущий конфиг отсутствует', 'text': 'Текущие настройки сохранятся в момент отстрела'}
            self.render("main.html", last_config=last_config, resp_count=db.response_log.count(), http_count=db.http_diff.count())

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
            (r"/", MainHandler),
            (r"/cc", CrossCheckHandler),
            (r"/newlog", NewLogsHandler),
            (r"/mongo_count", MongoHandler),

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
