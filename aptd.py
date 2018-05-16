#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

from common.core import initDB
from common.utils import rmdir

from parser.bro import *
from parser.yara import *
from parser.tcpflow import *
from parser.mime import *

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
        '''
        for i in os.listdir("http"):
            HttpParser.parse(i.read())
            if HTTPIDS.match(db, key, value):
                Traffic.add(db, dstport, srcport, srcip, dstip)
        '''
