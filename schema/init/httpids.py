#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(os.path.join("..", ".."))

from common.core import initDB
from schema.tables.httpids import HTTPIDS

db = initDB()

HTTPIDS.add("*", r"\.\.", "DirTraversal", "Low", "waf")
HTTPIDS.add("*", r"select.+(from)", "SQLi", "Medium", "waf")
HTTPIDS.add("*", r"(?:(union(.*?)select))", "SQLi", "Medium", "waf")
HTTPIDS.add("*", r"sleep\((\s*)(\d*)(\s*)\)", "SQLi", "Medium", "waf")
HTTPIDS.add("*", r"benchmark\((.*)\,(.*)\)", "SQLi", "Medium", "waf")
HTTPIDS.add("*", r"base64_decode\(", "SQLi", "Medium", "waf")
HTTPIDS.add("*", r"information_schema", "SQLi", "Medium", "waf")
HTTPIDS.add("*", r"into(\s+)+(?:dump|out)file\s*", "SQLi", "Medium", "waf")
HTTPIDS.add("*", r"group\s+by.+\(", "SQLi", "Medium", "waf")

HTTPIDS.add(
    "*",
    r"file_get_contents",
    "ReadFile", "Medium", "waf"
)

HTTPIDS.add(
    "*",
    r"file_put_contents",
    "WriteFile", "High", "waf"
)

HTTPIDS.add(
    "*",
    r"(?:define|eval|file_get_contents|chmod|include|require|require_once|shell_exec|phpinfo|system|passthru|preg_\w+|execute|echo|print|print_r|var_dump|(fp)open|alert|showmodaldialog)",
    "RCE", "High", "waf"
)

HTTPIDS.add(
    "*",
    r"/bin/bash|/bin/cat|/bin/echo",
    "Command Injection", "High", "waf"
)

HTTPIDS.add(
    "*",
    r"(gopher|doc|php|glob|file|phar|zlib|ftp|ldap|dict|ogg|data)\:\/",
    "SSRF", "Medium", "waf"
)

HTTPIDS.add(
    "*",
    r"\<(iframe|script|body|img|layer|div|meta|style|base|object|input)",
    "XSS", "Medium", "waf"
)

HTTPIDS.add("*", r"(onmouseover|onerror|onload)\=", "XSS", "Medium", "waf")
