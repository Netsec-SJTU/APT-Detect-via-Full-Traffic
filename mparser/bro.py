#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import uuid
import magic
import shutil
import subprocess

from common.path import Paths
from common.utils import isInternalIp


def bro(target):
    '''
    bro support dir extract
    '''
    ret = {
        "ip": set(),
        "domain": set(),
        "md5": set(),
        "sha1": set(),
    }
    print("run bro on %s" % target)
    os.chdir("pcap")
    cmd = " ".join([
        "bro", "-r", target,
        Paths.extractFileScript,
        Paths.fileHashScript
    ])
    os.system(cmd)
    if os.path.exists("conn.log"):
        with open("conn.log") as fh:
            for i in fh:
                if i.startswith("#"):
                    continue
                i = i.split("\t")
                srcip = i[2]
                dstip = i[4]
                if not isInternalIp(srcip):
                    ret["ip"].add(srcip)
                if not isInternalIp(dstip):
                    ret["ip"].add(dstip)
    if os.path.exists("dns.log"):
        with open("dns.log") as fh:
            for i in fh:
                if i.startswith("#"):
                    continue
                i = i.split("\t")
                if i[9] != "WUC":
                    ret["domain"].add(i[9])
    if os.path.exists("files.log"):
        with open("files.log") as fh:
            for i in fh:
                if i.startswith("#"):
                    continue
                i = i.split("\t")
                md5 = i[19]
                sha1 = i[20]
                if len(md5) > 1:
                    ret["md5"].add(i[9])
                if len(sha1) > 1:
                    ret["sha1"].add(i[9])
    os.system("rm -rf *.log")
    return ret


def extractBro(mimes):
    """extract file with specific mime

    Args:
        mimes (dict): key is mime, value is ext
    tshark -r smtp.pcap -z conv,tcp
    tshark -r smtp.pcap -z follow,tcp,raw,0
    """
    cnt = 0
    target = mimes.keys()

    if not os.path.exists("extract"):
        os.mkdir("extract")

    for f in os.listdir("extract_files"):
        mime = magic.from_file("./extract_files/%s" % f, mime=True)
        if mime in target:
            ext = mimes[mime]
            if not os.path.exists(os.path.join("extract", ext)):
                os.mkdir(os.path.join("extract", ext))
            shutil.copyfile("./extract_files/%s" % f, "./extract/%s/%s.%s" % (ext, cnt, ext))
            cnt += 1
            print("%s file %s" % (mime, f))
        else:
            print("skip %s with mime %s" % (f, mime))
