#!python3

import socket
from datetime import datetime


if __name__ == '__main__':
    addr = input("server address: ")
    send_to = (addr, 9999)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4, TCP

    client.connect(send_to)

    while True:
        message = input('send: ').encode('utf-8')
        client.sendall(message)
        answer = client.recv(8*1024*1024)
        print('{t}: response: {d}\n'.format(t = datetime.now(), d = answer.decode('utf-8')))
