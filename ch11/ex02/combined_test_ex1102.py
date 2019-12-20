import unittest
import zeromq_client as zeromq_client
import zeromq_server as zeromq_server


class MyTestCase(unittest.TestCase):
    def test_zero_mq(self):
        import datetime

        expected = datetime.datetime.now()

        import threading
        thread_1 = threading.Thread(target=zeromq_server.run_time_server)
        thread_1.start()

        server_ret_date = zeromq_client.connect_server()
        actual = datetime.datetime.strptime(server_ret_date, "%Y-%m-%d %H:%M:%S.%f")
        thread_1.join()

        self.assertEqual(expected.year, actual.year)
        self.assertEqual(expected.month, actual.month)
        self.assertEqual(expected.day, actual.day)

if __name__ == '__main__':
    unittest.main()
