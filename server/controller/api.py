#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.web

from server.controller.base import BaseHandler
from schema.tables.traffic import Traffic


class MainHandler(BaseHandler):

    def get(self):
        self.render("index.html")


class TrafficHandler(BaseHandler):

    def get(self):
        self.ok(Traffic.getAll())


class MalwareHandler(BaseHandler):

    def get(self):
        self.render("malware.html")


class SubmitHandler(BaseHandler):

    def get(self):
        self.render("submit.html")
