#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import uuid
import shutil
import time


def guid():
    return uuid.uuid4().hex


def rmdir(dir):
    if os.path.exists(dir):
        shutil.rmtree(dir)


def now():
    # 返回当前时间
    return time.strftime('%Y-%m-%d %X', time.localtime(time.time()))
