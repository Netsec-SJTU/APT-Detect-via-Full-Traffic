#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(os.path.join("..", ".."))

from common.core import initDB
from schema.tables.httpids import HTTPIDS

db = initDB()

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

for r in regexps:
    HTTPIDS.add(db, "*", r, "waf")
