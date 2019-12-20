import unittest
import tcp_server as tcp_server
from unittest import mock
import socket


class MockSocketServer:
    def __init__(self):
        self.bind_address = None
        self.listen_backlog = 0
        self.is_called_close = False
        self.recv_msg = b''

    def bind(self, address):
        self.bind_address = address

    def listen(self, backlog):
        self.listen_backlog = backlog

    def accept(self):
        return MockConnection(self.recv_msg), self.bind_address

    def close(self):
        self.is_called_close = True

    def set_recv_msg(self, recv_msg=b''):
        self.recv_msg = recv_msg


class MockConnection:
    def __init__(self, send_msg):
        self.send_msg = send_msg

    def sendall(self, recv_msg):
        pass

    def recv(self, maxsize=1000):
        return self.send_msg


def mock_socket_recv_msg_time(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0, fileno=None):
    mock_socket = MockSocketServer()
    mock_socket.set_recv_msg(b'time')
    return mock_socket


def mock_socket_recv_msg_not_time(family=socket.AF_INET, type=socket.SOCK_STREAM, proto=0, fileno=None):
    mock_socket = MockSocketServer()
    mock_socket.set_recv_msg(b'not_time')
    return mock_socket


def mock_datetime_now():
    return b'2019-11-13 00:00:00.000000'


class MyTestCase(unittest.TestCase):
    @mock.patch('socket.socket', side_effect=mock_socket_recv_msg_time)
    @mock.patch('tcp_server.get_time_now_by_bytes', side_effect=mock_datetime_now)
    def test_send_msg_when_recv_time(self, mock_socket, mock_datetime):
        expected = b'2019-11-13 00:00:00.000000'
        server = tcp_server.TcpServer()
        recv_msg, send_msg = server.run()
        self.assertEqual(expected, send_msg)

    @mock.patch('socket.socket', side_effect=mock_socket_recv_msg_not_time)
    def test_send_msg_when_recv_not_time(self, mock_socket):
        expected = b'Enter time'
        server = tcp_server.TcpServer()
        recv_msg, send_msg = server.run()
        self.assertEqual(expected, send_msg)



if __name__ == '__main__':
    unittest.main()
