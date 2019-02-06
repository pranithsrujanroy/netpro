# -*- coding: utf-8 -*-
"""
Created on Wed Feb 06 10:16:09 2019

@author: Student
"""

""" 
Question:
    Write a simple TCP echo client/server application with the help of TCP
socket object. The server waits for the client to be connected and send
some data to the server. When the data is received, the server echoes the
data to the client.
"""

import socket

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    port = 12345
    host = socket.gethostname()
    s.bind((host, port))
    s.listen(1)
    print('Server listening...')
    while True:
        c, addr = s.accept()
        c.settimeout(10)
        data = c.recv(1024)
        #if data:
        print("Server received the below data: \n %s" %data)
        c.send(data)
        c.close()
        break
    s.close()

if __name__ == "__main__":
    start_server()