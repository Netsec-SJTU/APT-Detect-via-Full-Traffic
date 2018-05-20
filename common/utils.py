#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import uuid
import shutil
import time
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
