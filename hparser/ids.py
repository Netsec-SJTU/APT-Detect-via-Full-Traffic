#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

class IDS(object):

    regexps = [
        r"\.\.",
        r"\:\$",
        r"\$\{",
        r"select.+(from)",
        r"(?:(union(.*?)select))",
        r"having|rongjitest",
        r"sleep\((\s*)(\d*)(\s*)\)",
        r"benchmark\((.*)\,(.*)\)",
        r"base64_decode\(",
        r"information_schema",
        r"(?:etc\/\W*passwd)",
        r"into(\s+)+(?:dump|out)file\s*",
        r"group\s+by.+\(",
        r"xwork.MethodAccessor",
        r"(?:define|eval|file_get_contents|include|require|require_once|shell_exec|phpinfo|system|passthru|preg_\w+|execute|echo|print|print_r|var_dump|(fp)open|alert|showmodaldialog)\(",
        r"(gopher|doc|php|glob|file|phar|zlib|ftp|ldap|dict|ogg|data)\:\/",
        r"java\.lang",
        r"\$_(GET|post|cookie|files|session|env|phplib|GLOBALS|SERVER)\[",
        r"\<(iframe|script|body|img|layer|div|meta|style|base|object|input)",
        r"(onmouseover|onerror|onload)\=",
    ]

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
