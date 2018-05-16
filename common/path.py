#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path as op


class Paths(object):

    base = op.dirname(
        op.dirname(op.abspath(__file__))
    )
    yaraRulePath = "/home/ubuntu/yara/rules/index.yar"
    broScriptPath = "/home/ubuntu/bro/scripts/policy/frameworks/files/extract-all-files.bro"


if __name__ == '__main__':
    print(Paths.base)
