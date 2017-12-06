import socket
from datetime import datetime

def handler(byte_data):
    data = byte_data.decode('utf-8')
    ret = ''
    if data == 'time':
        ret = str(datetime.now())
    elif data[-5:] == '#caps':
        ret = data[:-5].upper()
    else:
        ret = str(len(data))
    return ret.encode('utf-8')


if __name__ == '__main__':
    recf = ("", 9999)

    server_init = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # IPv4, TCP

    server_init.bind(recf)
    server_init.listen()

    stream_sock, __addr__ = server_init.accept()

    while True:
        data = stream_sock.recv(1024)
        print('{t}: message: {d}'.format(t = datetime.now(), d = data.decode('utf-8')))
        stream_sock.send(handler(data))