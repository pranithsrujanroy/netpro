# -*- coding: utf-8 -*-
"""
Created on Wed Feb 06 11:31:51 2019

@author: Student
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
s.connect(('127.0.0.1', 1233))
data = s.recv(1024)
print("Client recv: %s" %data)