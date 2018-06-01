#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import os
# import sys
# sys.path.append(os.path.join("..", ".."))

from common.utils import now
from schema.tables.malware import Malware
from schema.tables.traffic import Traffic

Traffic.add(
    53, 1325, "192.168.106.131", "192.168.106.2",
    "APT Domain", "High", "DNS", '2012-09-08 18:50:26', "APT-Report", "apt-o.pcap"
)

Traffic.add(
    80, 1413, "192.168.106.131", "69.194.193.34",
    "APT IP", "High", "HTTP", '2012-09-08 18:50:26', "APT-Report", "apt-o.pcap"
)

Traffic.add(
    80, 1413, "192.168.106.131", "69.194.193.34",
    "Low Entropy", "Low", "HTTP", '2012-09-08 18:50:26', "Abnormal", "apt-o.pcap"
)

Malware.add(
    "37d801882221dbc8f9da510e9531434ffb63faf61052c0263b658ca227b9a453",
    "java.jar", '2012-09-08 18:50:26', "ORIGINAL APT",
    "High", "Manual", "apt-o.pcap"
)

Malware.add(
    "0e80aa63d9069f8325ed4d66327270a8c063fe94485e5266c0bb2eb117fe2e05",
    "diJPN.exe", '2012-09-08 18:50:26', "ORIGINAL APT",
    "High", "Manual", "apt-o.pcap"
)

Malware.add(
    "0e80aa63d9069f8325ed4d66327270a8c063fe94485e5266c0bb2eb117fe2e05",
    "diJPN.exe", '2012-09-08 18:50:26', "Mal Imports",
    "Low", "Manual", "apt-o.pcap"
)

