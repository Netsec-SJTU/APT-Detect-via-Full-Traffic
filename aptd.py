#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Summary
"""
import os
import sys
import time
import shutil
import subprocess

import magic

from config import Config


def yara(target, rulepath=Config.yaraRulePath):
    if not os.path.isdir(target):
        os.system("yara -w %s %s" % (rulepath, target))
    for i in os.listdir(target):
        filepath = os.path.join(target, i)
        print("test %s" % filepath)
        os.system("yara -w %s %s" % (rulepath, filepath))


def bro(target):
    os.system("bro -r %s %s" % (target, Config.broScriptPath))


def extract(mimes):
    """extract file with specific mime

    Args:
        mimes (dict): key is mime, value is ext
    tshark -r smtp.pcap -z conv,tcp
    tshark -r smtp.pcap -z follow,tcp,raw,0
    """
    cnt = 0
    start = time.time()
    target = mimes.keys()

    for f in os.listdir("extract_files"):
        mime = magic.from_file("./extract_files/%s" % f, mime=True)
        if mime in target:
            ext = mimes[mime]
            if not os.path.exists(ext):
                os.mkdir(ext)
            shutil.copyfile("./extract_files/%s" % f, "./%s/%s.%s" % (ext, cnt, ext))
            cnt += 1
            print("%s file %s" % (mime, f))


def logmimes():
    """Summary
    """
    cnt = 0
    start = time.time()
    mimes = set()

    for f in os.listdir("extract_files"):
        mime = magic.from_file("./extract_files/%s" % f, mime=True)
        mimes.add(mime)
        cnt += 1
        if cnt % 1000 == 0:
            print "time %s, cnt %d, file: %s\n" % (time.time() - start, cnt, f),
            start = time.time()

    mimes = sorted(list(mimes))
    with open("mimes.log", "w") as w:
        for m in mimes:
            w.write(m+"\n")


def choiceMime(mtype):
    if mtype == "ms":
        return {
            "application/msword": "doc",
        }
    elif mtype == "zip":
        return {
            "application/gzip": "zip",
            "application/zip": "zip",
            "application/x-7z-compressed": "7z",
            "application/x-rar": "rar",
            "application/x-tar": "tar",
        }
    elif mtype == "audio":
        return {
            "audio/mp4": "mp4",
            "video/mp4": "mp4",
        }
    elif mtype == "image":
        return {
            "image/gif": "gif",
            "image/jpeg": "jpeg",
            "image/png": "png",
        }
    elif mtype == "jar":
        # android ana
        return {
            "application/jar": "jar",
        }
    elif mtype == "txt":
        return {
            "text/html": "html",
            "text/plain": "txt",
            "text/x-asm": "asm",
            "text/x-c": "c",
        }
    elif mtype == "exe":
        return {
            # exe
            # elf
        }
    else:
        return {}


def printHelp():
    print "python aptd.py log"
    print "python aptd.py clear"
    print "python aptd.py bro test.pcap"
    print "python aptd.py e image"
    print "python aptd.py all test.pcap"


def rmdir(dir):
    if os.path.exists(dir):
        shutil.rmtree(dir)


def tcpflow(file):
    os.system("tcpflow -r %s -e http -o output" % file)
    for i in os.listdir("output"):
        # if "HTTPBODY" not in i:
        if "HTTPBODY" in i:
            # os.move(os.path.join('output', i), os.path.join('httpbody', i))
            os.remove(os.path.join('output', i))
    # os.system("rm -rf ./output/!(*HTTPBODY*)")


def tcpflowfile():
    for i in os.listdir("output"):
        with open(os.path.join('output', i), "r") as fh:
            cnt = fh.read()
            if "HTTP" in cnt:
                print i
                print cnt
                raw_input("c?")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        printHelp()
    elif sys.argv[1] == "e":
        extract(choiceMime(sys.argv[2]))
    elif sys.argv[1] == "clear":
        removes = [
            "extract_files",
            "png",
            "jpeg",
            "gif",
            "mp4",
            "zip",
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
    elif sys.argv[1] == "all":
        # sys.argv[2] => pcap file path
        # extract file from traffic
        bro(sys.argv[2])
        # use IoC detect file
        yara(sys.argv[2])
        # split http flow
        # http flow => rule
        tcpflow(sys.argv[2])
