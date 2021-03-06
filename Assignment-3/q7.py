# -*- coding: utf-8 -*-
"""
Created on Wed Feb 06 09:57:47 2019

@author: Student
"""

"""
Question:
    Write a program that demonstrates the reuse socket addresses?
"""
import socket

def reuseaddr():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    reuse = s.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print("Default address reuse %d" %reuse)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    cur_reuse = s.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print("Current address reuse %d" %cur_reuse)
    
    port = 1233
    host = socket.gethostname()
    s.bind(('', port))
    s.listen(5)
    s.settimeout(10)
    print("Server listening on ", s.getsockname())
    while 1:
        try:
            conn, addr = s.accept()
            print("Connected to %s" %str(addr[0]))
            conn.send(b"Server says hi")
            conn.close()
            break
        except socket.error as msg:
            print("%s" %msg)
            break
    s.close()

if __name__ == "__main__":
    reuseaddr()