#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(os.path.join("..", ".."))

from common.core import initDB
from schema.tables.httpids import HTTPIDS

db = initDB()

HTTPIDS.add(db, "*", r"\.\.", "DirTraversal", "Low", "waf")
HTTPIDS.add(db, "*", r"select.+(from)", "SQLi", "Medium", "waf")
HTTPIDS.add(db, "*", r"(?:(union(.*?)select))", "SQLi", "Medium", "waf")
HTTPIDS.add(db, "*", r"sleep\((\s*)(\d*)(\s*)\)", "SQLi", "Medium", "waf")
HTTPIDS.add(db, "*", r"benchmark\((.*)\,(.*)\)", "SQLi", "Medium", "waf")
HTTPIDS.add(db, "*", r"base64_decode\(", "SQLi", "Medium", "waf")
HTTPIDS.add(db, "*", r"information_schema", "SQLi", "Medium", "waf")
HTTPIDS.add(db, "*", r"into(\s+)+(?:dump|out)file\s*", "SQLi", "Medium", "waf")
HTTPIDS.add(db, "*", r"group\s+by.+\(", "SQLi", "Medium", "waf")
HTTPIDS.add(
    db, "*",
    r"(?:define|eval|file_get_contents|include|require|require_once|shell_exec|phpinfo|system|passthru|preg_\w+|execute|echo|print|print_r|var_dump|(fp)open|alert|showmodaldialog)\(",
    "RCE", "High", "waf"
)
HTTPIDS.add(
    db, "*",
    r"(gopher|doc|php|glob|file|phar|zlib|ftp|ldap|dict|ogg|data)\:\/",
    "SSRF", "Medium", "waf"
)
HTTPIDS.add(
    db, "*",
    r"\<(iframe|script|body|img|layer|div|meta|style|base|object|input)",
    "XSS", "Medium", "waf"
)
HTTPIDS.add(db, "*", r"(onmouseover|onerror|onload)\=", "XSS", "Medium", "waf")
