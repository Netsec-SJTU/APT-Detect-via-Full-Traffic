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


def analyze(target):
    os.system("yara -w /home/ubuntu/yara/rules/index.yar %s" % target)


def bro(target):
    cmd = "bro -r %s /home/ubuntu/bro/scripts/policy/frameworks/files/extract-all-files.bro"
    os.system(cmd % target)


def extract(mimes):
    """extract file with specific mime

    Args:
        mimes (dict): key is mime, value is ext
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
    print "python extract.py log"
    print "python extract.py clear"
    print "python extract.py bro test.pcap"
    print "python extract.py e image"


def rmdir(dir):
    if os.path.exists(dir):
        shutil.rmtree(dir)


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
