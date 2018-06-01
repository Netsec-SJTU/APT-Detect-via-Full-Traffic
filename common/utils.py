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
    return sum(map(lambda i: - i*math.log(i, 2), x))
