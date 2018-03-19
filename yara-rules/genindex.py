#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def main():
    changeCondition()


def changeCondition():
    for i in os.listdir("APT"):
        cnt = ""
        with open(os.path.join("APT", i)) as fh:
            while True:
                line = fh.readline()
                if "condition:" in line:
                    cnt += line
                    cnt += " " * 8 + "any of them\n"
                    line = fh.readline()
                    line = line[:8] + "//" + line[8:]
                    cnt += line
                    line = fh.readline()
                elif line == "":
                    break
                cnt += line
        with open(os.path.join("APT", i), "wb") as fh:
            fh.write(cnt)

def genAPTIndex():
    cnt = ""
    for i in os.listdir("APT"):
        cnt += 'include "./APT/%s"\n' % i
    with open("index.yar", "w") as fh:
        fh.write(cnt)


def genhashIndex():
    cnt = ""
    for i in os.listdir("hash"):
        cnt += 'include "./hash/%s"\n' % i
    with open("index_hash.yar", "w") as fh:
        fh.write(cnt)


if __name__ == '__main__':
    main()
