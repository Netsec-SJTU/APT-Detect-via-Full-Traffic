#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from config import Config


def yara(target, rulepath=Config.yaraRulePath):
    if not os.path.isdir(target):
        os.system("yara -w %s %s" % (rulepath, target))
    for i in os.listdir(target):
        filepath = os.path.join(target, i)
        print("test %s" % filepath)
        os.system("yara -w %s %s" % (rulepath, filepath))
