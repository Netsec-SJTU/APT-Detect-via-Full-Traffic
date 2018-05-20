#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

from common.core import initDB
from common.utils import rmdir
from common.utils import now

from mparser.bro import *
from mparser.yara import *
from mparser.tcpflow import tcpflow
from mparser.mime import *
from mparser.http import HttpParser

from Trafficker.packets.pcap import Pcap
from Trafficker.handlers.tcp import tcpHandler

from schema.tables.httpids import HTTPIDS
from schema.tables.traffic import Traffic


def printHelp():
    print "python aptd.py log"
    print "python aptd.py clear"
    print "python aptd.py bro test.pcap"
    print "python aptd.py e image,js"
    print "python aptd.py all test.pcap"


def interactive(self):
    while True:
        cmd = raw_input(">>> ")
        if cmd in ["exit", "quit"]:
            return
        elif cmd == "help":
            printHelp()
        elif cmd == "bro":
            dst = raw_input("(dst) >>> ")
            bro(dst)
        elif cmd == "flow":
            dst = raw_input("(dst) >>> ")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        printHelp()
    elif sys.argv[1] == "e":
        if len(sys.argv) > 2:
            extractBro(choiceMime(sys.argv[2].split(",")))
        else:
            extractBro(choiceMime(["all"]))
    elif sys.argv[1] == "clear":
        removes = [
            "extract_files",
            "extract",
        ]
        for r in removes:
            rmdir(r)
    elif sys.argv[1] == "bro":
        bro(sys.argv[2])
    elif sys.argv[1] == "log":
        logmimes()
    elif sys.argv[1] == "yara":
        if len(sys.argv) > 3:
            yara(sys.argv[2], sys.argv[3])
        else:
            yara(sys.argv[2])
    elif sys.argv[1] == "flow":
        tcpflow(sys.argv[2])
    elif sys.argv[1] == "all":
        db = initDB()
        # sys.argv[2] => pcap file path
        # extract file from traffic
        bro(sys.argv[2])
        # use IoC detect file
        yara(sys.argv[2])
        # split http flow
        # http flow => rule
        tcpflow(sys.argv[2])
        Pcap(sys.argv[2], [])
    elif sys.argv[1] == "test":
        db = initDB()
        for i in os.listdir("tcpflow"):
            if "HTTP" in i:
                continue
            if i == "report.xml":
                continue
            if i == "alerts.txt":
                continue
            h = HttpParser()
            h.parse(open(os.path.join("tcpflow", i), "rb").read())
            # print(h.headers)
            if h.type == 2:
                # response
                continue
            try:
                src, dst = i.split("-")
            except Exception as e:
                print(e)
                print(i)
                continue
            srcip = ".".join(map(lambda i: str(int(i)), src.split(".")[:4]))
            srcport = int(src.split(".")[-1])
            dstip = ".".join(map(lambda i: str(int(i)), dst.split(".")[:4]))
            dstport = int(dst.split(".")[-1])
            comment = "QWB.pcap"
            tests = []
            if "user-agent" in h.headers:
                tests.append(["ua", h.headers["user-agent"][1]])
            tests.append(["url", h.url.path])
            tests.append(["*", h.url.query])
            tests.append(["*", h.body])
            tests.append(["*", h.build_all_header()])
            for t in tests:
                ret = HTTPIDS.match(t[0], t[1])
                if ret:
                    Traffic.add(
                        dstport, srcport, srcip, dstip,
                        ret.threat, ret.severity, "HTTP",
                        now(), ret.reference, comment
                    )
                    continue
