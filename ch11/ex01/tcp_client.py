import socket
from datetime import datetime


class TcpClient:
    def __init__(self, url='127.0.0.1', port=6789):
        self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__address = (url, port)
        self.__max_size = 1000

    def run(self, send_msg: bytes = b'time') -> bytes:
        address = self.__address
        self.__client.connect(address)
        self.__client.sendall(send_msg)
        recv_msg = self.__client.recv(self.__max_size)
        self.__client.close()
        return recv_msg, send_msg

