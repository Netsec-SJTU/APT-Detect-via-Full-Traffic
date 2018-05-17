#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import tornado.web

from schema.tables.base import DBSession

class BaseHandler(tornado.web.RequestHandler):

    def on_finish(self):
        # every thread should has its own session
        # no... there is a bug
        # will double free 2333
        # 并发就炸了 
        db = DBSession()
        db.flush()
        db.close()
        db.remove()
        DBSession._db = None

    def ok(self, data):
        self.set_header('Content-Type', 'application/json; charset="utf-8"')
        self.write(json.dumps({"status": "ok", "data": data}))

    def error(self, status_code, msg):
        self.set_header('Content-Type', 'application/json; charset="utf-8"')
        self.set_status(status_code)
        self.write(json.dumps({"msg": msg}))
