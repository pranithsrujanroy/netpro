# -*- coding: utf-8 -*-
"""
Created on Wed Feb 06 10:16:58 2019

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

def start_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 12345
    host = socket.gethostname()
    s.connect((host, port))
    try:
        msg = "Hello server...echo me this message!"
        print("Client sent: %s" %msg)
        s.send(msg)
        amt_recv = 0
        l = len(msg)
        while amt_recv < l:
            data = s.recv(5)
            amt_recv += len(data)
            print("%s" %data)
    except socket.errno, e:
        print("Socket error: %s" %str(e))
    except Exception, e:
        print("%s" %str(e))
    finally:
        print("Closing connection by client...")
        s.close()

if __name__ == "__main__":
    start_client()