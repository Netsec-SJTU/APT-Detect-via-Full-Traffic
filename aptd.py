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
    '''
    bro support dir extract
    '''
    print("try bro %s" % target)
    os.system("bro -r %s %s" % (os.path.join(target, i), Config.broScriptPath))


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


def choiceMime(mtype=[]):
    ret = {}
    if "ms" in mtype or "all" in mtype:
        ret.update({
            "application/msword": "doc",
        })
    if "zip" in mtype or "all" in mtype:
        ret.update({
            "application/gzip": "zip",
            "application/zip": "zip",
            "application/x-7z-compressed": "7z",
            "application/x-rar": "rar",
            "application/x-tar": "tar",
            "application/vnd.ms-cab-compressed": "cab",
        })
    if "audio" in mtype or "all" in mtype:
        ret.update({
            "audio/mp4": "mp4",
            "video/mp4": "mp4",
        })
    if "image" in mtype or "all" in mtype:
        ret.update({
            "image/gif": "gif",
            "image/jpeg": "jpeg",
            "image/png": "png",
        })
    if "jar" in mtype or "all" in mtype:
        # android ana
        ret.update({
            "application/jar": "jar",
        })
    if "txt" in mtype or "all" in mtype:
        ret.update({
            "text/html": "html",
            "application/xml" : "xml",
            "text/plain": "txt",
            "text/x-asm": "asm",
            "text/x-c": "c",
        })
    if "exe" in mtype or "all" in mtype:
        ret.update({
            # exe
            # elf
        })
    if "bin" in mtype or "all" in mtype:
        ret.update({
            "application/octet-stream": "bin"
        })

    return ret


def printHelp():
    print "python aptd.py log"
    print "python aptd.py clear"
    print "python aptd.py bro test.pcap"
    print "python aptd.py e image,js"
    print "python aptd.py all test.pcap"


def rmdir(dir):
    if os.path.exists(dir):
        shutil.rmtree(dir)


def tcpflow(target, outdir="output"):
    if os.path.isdir(target):
        for i in os.listdir(target):
            if not i.endswith(".pcap"):
                continue
            tcpflow(os.path.join(target, i))

    os.system("tcpflow -r %s -e http -o %s" % (target, dir))
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
                raw_input("continue?")


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
            extract(choiceMime(sys.argv[2].split(",")))
        else:
            extract(choiceMime(["all"]))
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
