#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(os.path.join("..", ".."))

from common.utils import now
from schema.tables.domainids import DomainIDS

# DomainIDS.add("baidu.com", "test")
# DomainIDS.add("t.cn", "test")
DomainIDS.add("www.java.com", "test")

print(DomainIDS.getAllDomains())
print(DomainIDS.getAllWithKey())
