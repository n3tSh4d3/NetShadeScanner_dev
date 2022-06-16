#!/bin/python3
import socket
import threading
import time
def scan_port(host,port):
    sk = socket.socket()
    sk.settimeout(0.5)
    conn_result = sk.connect_ex((host, port))
    print(f' test {port} port')
    if conn_result == 0:
        print(f' The server {host} Of {port} Port is open ')
    sk.close()
# 8.129.162.225
start_time = time.time()
host = input(' Please enter the server ip Address :')
thread_list = []
for port in range(0, 65536):
    t = threading.Thread(target=scan_port, args=(host, port))
    thread_list.append(t)
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()
    end_time = time.time()
    print(f' Time consuming :{end_time-start_time}')