# -*- coding: utf-8 -*-
"""
Created on Wed Feb 06 09:32:03 2019

@author: Student
"""

"""
Question:
    Modifying sockets send/receive buffer size and changing the socket to
blocking/non-blocking mode?
"""

import socket

SEND_BUFF_SIZE = 1024
RECV_BUFF_SIZE = 2048

def modify_buff_size():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    curr_buff_size = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Default send buffer size is %d" %curr_buff_size)
    
    s.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_BUFF_SIZE)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, RECV_BUFF_SIZE)
    
    buff_size = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Send buffer size set to %d" %buff_size)
    
def block_test():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_BUFF_SIZE)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, RECV_BUFF_SIZE)
    host = socket.gethostname()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, 1235))
    print("Server listening...")
    s.listen(5)
    while(1):
        conn, addr = s.accept()		# accept the connection
        s.setblocking(0)
        print("Receiving data...")
        data = conn.recv(1024)	
        while data:			        # till data is coming
            #print(data.decode('utf-8'))
            data = conn.recv(1024)
        print("All Data Received")	# Will execute when all data is received
        conn.close()
        break
    s.close()
    
if __name__ == "__main__":
    modify_buff_size()
    block_test()