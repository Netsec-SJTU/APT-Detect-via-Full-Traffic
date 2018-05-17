#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess

from common.path import Paths
from schema.tables.fileids import FILEIDS


def yara(target, rulepath=Paths.yaraRulePath):
    # if not os.path.isdir(target):
        # os.system("yara -w %s %s" % (rulepath, target))
    # for i in os.listdir(target):
        # filepath = os.path.join(target, i)
    print("run yara on %s" % target)
    p = subprocess.Popen(["yara", "-w", rulepath, target], stdout=subprocess.PIPE)
    p = p.communicate()[0]
    p = p.decode('utf8').split('\n')
    for l in p:
        ret = l.split()
        if len(ret) != 2:
            continue
        mtype, filename = ret
        
