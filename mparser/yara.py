#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from common.path import Paths


def yara(target, rulepath=Paths.yaraRulePath):
    # if not os.path.isdir(target):
        # os.system("yara -w %s %s" % (rulepath, target))
    # for i in os.listdir(target):
        # filepath = os.path.join(target, i)
    print("run yara on %s" % filepath)
    os.system("yara -w %s %s" % (rulepath, filepath))
