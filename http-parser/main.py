#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mparser import HttpParser
from pprint import pprint

if __name__ == '__main__':
    h = HttpParser()
    cnt = open("./sample/1.txt", "rb").read()
    # print cnt.encode("hex")
    h.parse(cnt)
    # print h.raw
    print h.method
    print h.url.query
    print h.headers['cookie'][1]
    print h.headers['user-agent'][1]
    # print h.chunker
    
    print "-" * 5
    exit()
    h2 = HttpParser(2)
    cnt = open("./sample/2.txt", "rb").read()
    h2.parse(cnt)
    print h2.code
    print h2.version
    print h2.body