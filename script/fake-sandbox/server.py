#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import socket
import time

HOST = '192.168.10.1'
PORT = 10888

for i in range(77):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    while True:
        j = str(i)
        data = conn.recv(1024)
        data = data.decode('utf-8')
        if data == 'SendVirusName':
            conn.sendall(j.encode('utf-8'))
            break
    conn.close()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024)
        data = data.decode('utf-8')
        if data == 'AnalysisComplete':
            print('Analysis Complete, Restarting...')
            time.sleep(25)
            os.system('C:\\Users\\Administrator\\Desktop\\powerup.bat')
            break
    conn.close()
