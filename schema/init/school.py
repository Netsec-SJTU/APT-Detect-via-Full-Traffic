#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import os
# import sys
# sys.path.append(os.path.join("..", ".."))

from common.utils import now
from schema.tables.traffic import Traffic

Traffic.add(
    80, 55431, "192.168.66.138", "218.78.185.210",
    "SQL", "High", "HTTP", now(), "waf", "school.pcap"
)

Traffic.add(
    80, 43187, "192.168.57.147", "180.153.105.158",
    "SQL", "High", "HTTP", now(), "waf", "school.pcap"
)

Traffic.add(
    80, 34792, "192.168.67.207", "180.97.168.187",
    "XSS", "High", "HTTP", now(), "waf", "school.pcap"
)

Traffic.add(
    80, 51439, "192.168.186.1", "122.228.238.153",
    "SQL", "High", "HTTP", now(), "waf", "school.pcap"
)

Traffic.add(
    80, 57201, "192.168.57.147", "180.153.105.158",
    "SQL", "High", "HTTP", now(), "waf", "school.pcap"
)

Traffic.add(
    80, 39311, "192.168.61.252", "203.100.92.155",
    "XSS", "High", "HTTP", now(), "waf", "school.pcap"
)

Traffic.add(
    8080, 50591, "192.168.65.52", "183.3.225.58",
    "DirTraversal", "High", "HTTP", now(), "waf", "school.pcap"
)


Traffic.add(
    80, 51248, "192.168.65.52", "140.205.218.67",
    "XSS", "High", "HTTP", now(), "waf", "school.pcap"
)


Traffic.add(
    80, 49542, "192.168.57.147", "180.153.105.166",
    "SQL", "High", "HTTP", now(), "waf", "school.pcap"
)


Traffic.add(
    80, 11112, "192.168.57.25", "14.17.32.229",
    "XSS", "High", "HTTP", now(), "waf", "school.pcap"
)


Traffic.add(
    80, 43554, "192.168.57.147", "180.153.105.158",
    "SQL", "High", "HTTP", now(), "waf", "school.pcap"
)

