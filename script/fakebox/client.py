#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import requests


class Client(object):

    def __init__(self, url):
        super(Client, self).__init__()
        self.url = url
        self.s = requests.Session()

    def runSample(self):
        r = self.s.get(self.url + "sample")
        virus = r.text
        r = self.s.get(self.url + "static/" + virus)
        if r.status_code != 200:
            os.system("start shutdown -s -t 00")
            print("error!!!")
            return
        elif virus == "no...":
            os.system("start shutdown -s -t 00")
            return
        with open(virus + ".exe", "wb") as fh:
            fh.write(r.content)
        os.system("fakenet64.exe")
        time.sleep(10)
        os.system(virus + ".exe")
        time.sleep(60)
        os.system("start taskkill /im fakenet64.exe")
        time.sleep(2)
        for filename in os.listdir("."):
            if filename.endswith(".pcap"):
                self.s.post(
                    self.url+"pcap",
                    data={"filename": virus}
                    files={"upfile": open(filename, "rb")}
                )
        r = self.s.get(self.url+"complete")
        os.system("start shutdown -s -t 00")


if __name__ == '__main__':
    url = "http://192.168.26.1:8888/"
    c = Client(url)
    c.runSample()
