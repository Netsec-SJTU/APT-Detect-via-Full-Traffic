#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(os.path.join("..", ".."))

from common.utils import now
from schema.tables.ipids import IPIDS

IPIDS.add("92.43.108.70", "test")
print(IPIDS.getAllWithKey())
