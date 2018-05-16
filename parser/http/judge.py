#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ids import IDS


def judge(h):
    for param in h.url.split("&"):
        key, value = param.split("=")
        if IDS.match(value):
            return True
    if IDS.match(h.headers['cookie'][1]):
        return True
    if IDS.match(h.url):
        return True
    if IDS.match(h.headers['user-agent'][1]):
        return True
    return False
