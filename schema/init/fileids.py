#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(os.path.join("..", ".."))

from common.utils import now
from schema.tables.fileids import FileIDS

FileIDS.add("WebShell", "e0ae520743d60096eda6b787c3f23a93",
            "e75de735c7a058443b5094f070a12a37f57fe748", "High", "Test")
print(FileIDS.getAllWithKey())
