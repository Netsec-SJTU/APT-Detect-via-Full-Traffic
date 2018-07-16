#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import uuid
import shutil
import time
import math
import hashlib


def guid():
    return uuid.uuid4().hex


def rmdir(dir):
    if os.path.exists(dir):
        shutil.rmtree(dir)


def now():
    # 返回当前时间
    return time.strftime('%Y-%m-%d %X', time.localtime(time.time()))


def filesha256(path):
    with open(path, 'rb') as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def entropy(x):
    '''calc entropy with a given list
    '''
    if isinstance(x, str):
        x = list(x)
        xlen = float(len(x))
        sets = set(x)
        ret = []
        for i in sets:
            ret.append(x.count(i) / xlen)
        x = ret
    return sum(map(lambda i: - i * math.log(i, 2), x))


def isInternalIp(ip):

    # https://en.wikipedia.org/wiki/Private_network

    priv_lo = re.compile("^127\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    priv_24 = re.compile("^10\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    priv_20 = re.compile("^192\.168\.\d{1,3}.\d{1,3}$")
    priv_16 = re.compile("^172.(1[6-9]|2[0-9]|3[0-1]).[0-9]{1,3}.[0-9]{1,3}$")

    return priv_lo.match(ip) or priv_24.match(ip)\
        or priv_20.match(ip) or priv_16.match(ip) \
        or ip == "localhost"
