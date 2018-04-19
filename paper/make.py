#!/usr/bin/env python
# -*- coding: utf-8 -*-

content = b""
for i in range(10):
    with open("%d.md" % i, "rb") as fh:
        content += fh.read()

with open("paper.md", "w") as fh:
    fh.write(content.decode("utf8"))
