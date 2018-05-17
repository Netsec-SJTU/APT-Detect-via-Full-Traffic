#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import tornado.web

from schema.tables.base import DBSession

class BaseHandler(tornado.web.RequestHandler):

    def initialize(self):
        DBSession(True)

    def on_finish(self):
        db = DBSession()
        db.flush()
        db.close()
        db.remove()
        del DBSession._db

    def ok(self, data):
        self.set_header('Content-Type', 'application/json; charset="utf-8"')
        self.write(json.dumps({"status": "ok", "data": data}))

    def error(self, status_code, msg):
        self.set_header('Content-Type', 'application/json; charset="utf-8"')
        self.set_status(status_code)
        self.write(json.dumps({"msg": msg}))
