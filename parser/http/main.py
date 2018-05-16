#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from mparser import HttpParser
from pprint import pprint


def test():
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

    h2 = HttpParser(2)
    cnt = open("./sample/2.txt", "rb").read()
    h2.parse(cnt)
    print h2.code
    print h2.version
    print h2.body


def test2(dir):
    h = HttpParser()
    dst = open("querys.txt", "wb")
    for i in os.listdir(dir):
        with open(os.path.join(dir, i), "r") as fh:
            cnt = fh.read()
            if "HTTP" not in cnt or cnt.startswith("HTTP"):
                continue
            h.parse(cnt)
            '''
            print cnt
            print "=" * 10
            print "Method", h.method
            print "Query", h.url.query
            if 'cookie' in h.headers:
                print "Cookie", h.headers['cookie'][1]
            if 'user-agent' in h.headers:
                print "UA", h.headers['user-agent'][1]
            print "=" * 10
            '''
            try:
                dst.write(h.url.query+"\n")
            except Exception as e:
                print i, len(cnt)
                raw_input("continue?")
            h.refresh()
            # raw_input("continue?")
    dst.close()


def test3():
    dst = open("querys.txt")
    bak = open("querys.tmp.txt", "wb")
    for i in dst:
        if i == "\n":
            continue
        else:
            bak.write(i)
    bak.close()
    dst.close()
    os.remove("querys.txt")
    os.rename("querys.tmp.txt", "querys.txt")


if __name__ == '__main__':
    # test2("/home/ubuntu/test/test/output")
    test3()
