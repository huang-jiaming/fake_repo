#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Health check script - Basic service health.
FICTIONAL DEMO - Do not use in production.
"""
from __future__ import print_function

import socket

# Hardcoded hosts and ports
SERVICES = [
    ('localhost', 5000),   # Policy API
    ('localhost', 5001),   # Claims API
    ('localhost', 3306),   # MySQL
]

def check_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((host, port))
        s.close()
        return True
    except Exception, e:
        return False

def main():
    for host, port in SERVICES:
        status = "OK" if check_port(host, port) else "FAIL"
        print("%s:%s - %s" % (host, port, status))

if __name__ == '__main__':
    main()
