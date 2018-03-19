#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def main():
    cnt = ""
    for i in os.listdir("APT"):
        cnt += 'include "./APT/%s"\n' % i
    with open("index.yar", "w") as fh:
        fh.write(cnt)

    cnt = ""
    for i in os.listdir("hash"):
        cnt += 'include "./hash/%s"\n' % i
    with open("index_hash.yar", "w") as fh:
        fh.write(cnt)

if __name__ == '__main__':
    main()
