#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def tcpflow(target, outdir="tcpflow"):
    if os.path.isdir(target):
        for i in os.listdir(target):
            if not i.endswith(".pcap"):
                continue
            tcpflow(os.path.join(target, i))

    os.system("tcpflow -r %s -e http -o %s" % (target, dir))
    # for i in os.listdir("tcpflow"):
        # if "HTTPBODY" not in i:
        # if "HTTPBODY" in i:
            # os.move(os.path.join('output', i), os.path.join('httpbody', i))
            # os.remove(os.path.join('tcpflow', i))
    # os.system("rm -rf ./output/!(*HTTPBODY*)")


def tcpflowfile():
    for i in os.listdir("tcpflow"):
        with open(os.path.join("tcpflow", i), "r") as fh:
            cnt = fh.read()
            if "HTTP" in cnt:
                print i
                print cnt
                raw_input("continue?")
