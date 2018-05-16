#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import uuid
import shutil


def guid():
    return uuid.uuid4().hex


def rmdir(dir):
    if os.path.exists(dir):
        shutil.rmtree(dir)
