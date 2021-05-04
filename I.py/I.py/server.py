import socket
import os
from _thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 2000))

print('Socket is listening..')
while True:
    server.listen()
    conn, addr = server.accept()
    print('connected by', addr)
    data = conn.recv(1)
    print(data)
