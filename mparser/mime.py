#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import magic


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
            "application/xml": "xml",
            "text/plain": "txt",
            "text/x-asm": "asm",
            "text/x-c": "c",
        })
    if "exe" in mtype or "all" in mtype:
        ret.update({
            "application/x-dosexec": "exe"
            # elf
        })
    if "bin" in mtype or "all" in mtype:
        ret.update({
            "application/octet-stream": "bin"
        })
    if "pdf" in mtype or "all" in mtype:
        ret.update({
            "application/pdf": "pdf"
        })
    if "swf" in mtype or "all" in mtype:
        ret.update({
            "application/x-shockwave-flash": "pdf"
        })
    return ret


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
            w.write(m + "\n")
