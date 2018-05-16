#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

class IDS(object):

    # learn from waf


    @classmethod
    def match(cls, s):
        for reg in cls.regexps:
            if re.match(reg, s, re.I):
                return True
        return False

if __name__ == '__main__':
    print IDS.match("../../../etc/passwd") == True
    print IDS.match(":$") == True
    print IDS.match(":x") == False
    print IDS.match("${") == True
    print IDS.match("select from ") == True
    print IDS.match("selEct from ") == True
    print IDS.match("union select") == True
    print IDS.match("union sElect") == True
    print IDS.match("HAVE") == False
    print IDS.match("HAVing") == True
    print IDS.match("sleep(10)") == True
    print IDS.match("sleep( 1 )") == True
    print IDS.match("benchmark( 1,1 )") == True
    print IDS.match("base64_decode(") == True
    print IDS.match("etc/passwd") == True
