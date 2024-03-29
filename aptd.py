#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
import datetime

from common.core import initDB
from common.utils import rmdir
from common.utils import now

'''
from mparser.bro import *
from mparser.yara import *
from mparser.tcpflow import tcpflow
from mparser.mime import *
from mparser.http import HttpParser
'''

from Trafficker.packets.pcap import Pcap
from Trafficker.handlers.tcp import tcpHandler

from schema.tables.httpids import HTTPIDS
from schema.tables.traffic import Traffic
from schema.tables.malware import Malware
from schema.tables.ipids import IPIDS
from schema.tables.domainids import DomainIDS
from schema.tables.fileids import FileIDS


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


def old():
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
            "tcpflow",
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
            '''
            h = HttpParser()
            h.parse(open(os.path.join("tcpflow", i), "rb").read())
            # print(h.headers)
            if h.type == 2:
                # response
                continue
            '''
            cnt = open(os.path.join("tcpflow", i), "rb").read()
            if cnt.startswith("HTTP"):
                continue
            ret = i.split("-")
            if len(ret) > 1:
                src = ret[0]
                dst = ret[1]
            else:
                continue
            srcip = ".".join(map(lambda i: str(int(i)), src.split(".")[:4]))
            srcport = int(src.split(".")[-1])
            dstip = ".".join(map(lambda i: str(int(i)), dst.split(".")[:4]))
            dstport = int(dst.split(".")[-1])
            comment = "QWB.pcap"
            ret = HTTPIDS.match("*", cnt)
            if ret:
                Traffic.add(
                    dstport, srcport, srcip, dstip,
                    ret.threat, ret.severity, "HTTP",
                    now(), ret.reference, comment
                )
                continue


def main():
    bro(sys.argv[1])
    maldomains = DomainIDS.getAllWithKey()
    malips = IPIDS.getAllWithKey()
    malfiles = FileIDS.getAllWithKey()
    os.chdir("pcap")
    if os.path.exists("conn.log"):
        with open("conn.log") as fh:
            for i in fh:
                if i.startswith("#"):
                    continue
                i = i.split("\t")
                srcip = i[2]
                dstip = i[4]
                if srcip not in malips:
                    if dstip not in malips:
                        continue
                    else:
                        reference = malips[dstip]
                else:
                    reference = malips[srcip]
                srcport = i[3]
                dstport = i[5]
                if i[7] == "-":
                    # tcp / udp
                    proto = i[6]
                else:
                    # http / dns
                    proto = i[7]
                Traffic.add(dstport, srcport, srcip, dstip,
                            "Mal IP", "HIGH", proto,
                            datetime.datetime(*time.localtime(float(i[0]))[:6]),
                            reference, "")
    if os.path.exists("dns.log"):
        with open("dns.log") as fh:
            for i in fh:
                if i.startswith("#"):
                    continue
                i = i.split("\t")
                if i[9] in maldomains:
                    Traffic.add(i[5], i[3], i[2], i[4],
                                "Mal Domain", "HIGH", "DNS",
                                datetime.datetime(*time.localtime(float(i[0]))[:6]),
                                maldomains[i[9]], i[9])
    if os.path.exists("files.log"):
        with open("files.log") as fh:
            for i in fh:
                if i.startswith("#"):
                    continue
                i = i.split("\t")
                md5 = i[19]
                sha1 = i[20]
                print(i[9])
                if md5 in malfiles:
                    Malware.add(i[9], datetime.datetime(*time.localtime(float(i[0]))[:6]),
                                malfiles[md5].mtype, malfiles[md5].severity, malfiles[md5].reference, "comment")


if __name__ == '__main__':
    main()
