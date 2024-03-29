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
    '''bro support dir extract
    '''
    print("run bro on %s" % target)
    os.chdir("pcap")
    cmd = " ".join([
        "bro", "-r", target,
        Paths.extractFileScript,
        Paths.fileHashScript
    ])
    os.system(cmd)


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
