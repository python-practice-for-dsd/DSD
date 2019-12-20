import unittest
import tcp_client as tcp_client
import tcp_server as tcp_server


class MyTestCase(unittest.TestCase):
    def test_send_msg_when_server_recv_time(self):
        import datetime
        expectedFormat = "%Y-%m-%dT%H:%M:%S.%f"

        import threading
        thread_1 = threading.Thread(target=tcp_server.TcpServer().run)
        thread_1.start()

        recv_msg, send_msg = tcp_client.TcpClient().run()
        # expectedFormat以外の文字列が来るとValueError Exceptionが発生してテストがFailする
        actual = datetime.datetime.strptime(recv_msg.decode('utf-8'), expectedFormat)
        thread_1.join()

    def test_send_msg_when_server_recv_not_time(self):
        expected = b'Enter time'

        import threading
        thread_1 = threading.Thread(target=tcp_server.TcpServer().run)
        thread_1.start()

        recv_msg, send_msg = tcp_client.TcpClient().run(b'not_time')
        thread_1.join()
        self.assertEqual(expected, recv_msg)

if __name__ == '__main__':
    unittest.main()
