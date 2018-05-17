#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.web

from server.controller.base import BaseHandler
from schema.tables.traffic import Traffic
from schema.tables.malware import Malware


class MainHandler(BaseHandler):

    def get(self):
        self.render("index.html")


class TrafficHandler(BaseHandler):

    def get(self):
        self.ok(Traffic.getPage())


class MalwareHandler(BaseHandler):

    def get(self):
        self.ok(Malware.getPage())


class SubmitHandler(BaseHandler):

    def get(self):
        self.render("submit.html")
