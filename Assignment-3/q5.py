# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 10:43:23 2019

@author: Pranith Srujan Roy
"""

"""
Question:
    Printing the current time from the internet time server with the help of NTP?
    Also write an SNTP client that prints the current time from the internet time server
    received with the SNTP protocol?
 """
import socket
import ntplib
import logging
from time import ctime

def print_time():
    ntp_client = ntplib.NTPClient()
    try:
        response = ntp_client.request('www.google.com')
        print ctime(response.tx_time)
    except (ntplib.NTPException, socket.gaierror) as e:
        #print(e)
        logging.error('NTP client request error: %s', str(e))
    
if __name__ == '__main__':
    print_time()