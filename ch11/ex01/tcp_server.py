import socket
import datetime


class TcpServer:
    def __init__(self, url='localhost', port=6789):
        address = (url, port)
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(address)
        self.__server = server

    def run(self, max_size=1000) -> bytes:
        self.__server.listen(1)
        client, address = self.__server.accept()

        recv_msg = client.recv(max_size)
        send_msg = self.__make_send_msg(recv_msg)

        client.sendall(send_msg)
        self.__server.close()
        return recv_msg, send_msg

    @staticmethod
    def __make_send_msg(recv_msg: bytes) -> bytes:
        if recv_msg.decode('utf-8') == 'time':
            send_msg = get_time_now_by_bytes()
        else:
            send_msg = b'Enter time'
        return send_msg


def get_time_now_by_bytes():
    return datetime.datetime.now().isoformat().encode('utf-8')
