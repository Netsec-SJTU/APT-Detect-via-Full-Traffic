#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import requests
import logging


class Client(object):

    def __init__(self, url):
        super(Client, self).__init__()
        self.url = url
        self.s = requests.Session()
        self.initLog()

    def initLog(self):
        formatStr = '[%(asctime)s] [%(levelname)s] %(message)s'
        logger = logging.getLogger("logger")
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(formatStr)
        ch = logging.StreamHandler()
        chformatter = logging.Formatter(formatStr)
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(chformatter)
        logger.addHandler(ch)
        self.logger = logger


    def runSample(self):
        self.logger.debug("ready to start...")
        time.sleep(10)
        self.logger.debug("get sample...")
        r = self.s.get(self.url + "sample")
        virus = r.text
        r = self.s.get(self.url + "static/" + virus)
        if not virus.endswith(".exe"):
            virus = virus + ".exe"
        if r.status_code != 200:
            self.logger.error("error, will shutdown")
            os.system("start shutdown -s -t 60")
            return
        elif virus == "no...":
            self.logger.error("error, will shutdown")
            os.system("start shutdown -s -t 60")
            return
        with open(virus, "wb") as fh:
            fh.write(r.content)
        # ---------------------------------
        self.logger.debug("run fakenet")
        os.system("start fakenet64.exe")
        time.sleep(10)
        self.logger.debug("run virus")
        os.system("start " + virus)
        time.sleep(60)
        os.system("start taskkill /im fakenet64.exe")
        time.sleep(2)
        self.logger.debug("run finish, upload pcap")
        # ---------------------------------
        for filename in os.listdir("."):
            if filename.endswith(".pcap"):
                self.s.post(
                    self.url+"pcap",
                    data={"filename": virus},
                    files={"upfile": open(filename, "rb")}
                )
        self.complete()

    def complete(self):
        self.logger.debug("complete")
        r = self.s.get(self.url + "complete")
        os.system("start shutdown -s -t 00")


if __name__ == '__main__':
    url = "http://192.168.26.1:8888/"
    c = Client(url)
    c.runSample()
