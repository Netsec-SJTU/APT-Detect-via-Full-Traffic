#!/usr/bin/env python
# -*- coding:utf-8 -*-

import tornado.web
from server.controller.base import BaseHandler


class MainHandler(BaseHandler):

    def get(self):
        self.render("index.html")


class TrafficHandler(BaseHandler):

    def get(self):
        self.render("traffic.html")

class MalwareHandler(BaseHandler):

    def get(self):
        self.render("malware.html")

class SubmitHandler(BaseHandler):

    def get(self):
        self.render("submit.html")
