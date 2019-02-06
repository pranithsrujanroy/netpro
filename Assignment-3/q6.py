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
    curr_buff_size = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Default send buffer size is %d" %curr_buff_size)
    
    s.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_BUFF_SIZE)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, RECV_BUFF_SIZE)
    
    buff_size = s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print("Send buffer size set to %d" %buff_size)
    
def block_test():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(1)
    s.settimeout(10)
    s.bind(("127.0.0.1", 1233))
    
    socket_addr = s.getsockname()
    print("Server listening...")
    s.listen(1)
    while(1):
        try:
            conn, addr = s.accept()
            print("Connected to %s" %str(addr))
            conn.send("Server says hi")
        except KeyboardInterrupt:
            break
        except socket.error, msg:
            print("%s" %msg)
            break
    s.close()
    
if __name__ == "__main__":
    modify_buff_size()
    block_test()