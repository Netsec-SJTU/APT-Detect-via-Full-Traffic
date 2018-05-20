#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import os
# import sys
# sys.path.append(os.path.join("..", ".."))

from common.utils import now
from schema.tables.malware import Malware
from schema.tables.traffic import Traffic

Traffic.add(
    80, 55342, "192.168.33.128", "104.171.117.216",
    "APT", "High", "HTTP", now(), "APT-Report", "apt.pcap"
)

Traffic.add(
    80, 55342, "192.168.33.128", "104.171.117.216",
    "Hang HTTP Request", "Low", "HTTP", now(), "Abnormal", "apt.pcap"
)

Malware.add(
    "79A508BA42247DDF92ACCBF5987B1FFC7BA20CD11806D332979D8A8FE85ABB04",
    "4F92D364CE871C1AEBBF3C5D2445C296EF535632.exe", now(), "APT 28 Dropper",
    "High", "Manual", "apt.pcap"
)
