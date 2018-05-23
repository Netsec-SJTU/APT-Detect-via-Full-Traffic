#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import subprocess

from uuid import uuid4

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session, flash

app = Flask(__name__)

app.secret_key = 'ChiAyTEcAd4ftVF3Jg8APOfZ4AAb4FPl'


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/sample")
def sample():
    for i in os.listdir("static"):
        if not i.endswith(".done") and \
                os.path.exists("static/" + i) and \
                not os.path.exists("static/" + i + ".done"):
            return i
    return "no..."


@app.route("/complete")
def complete():
    time.sleep(25)
    os.system('start c.bat')
    return "ok..."


@app.route("/pcap", methods=['POST'])
def pcap():
    filename = request.form["filename"]
    f = request.files['upfile']
    f.save("pcaps/" + filename + uuid4().hex[:5] + ".pcap")
    with open("static/" + filename + ".done", "wb") as fh:
        pass
    return "ok..."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
