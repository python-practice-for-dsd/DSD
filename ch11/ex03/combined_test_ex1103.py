import unittest
import xmlrpc_client as xmlrpc_client
import xmlrpc_server as xmlrpc_server


class MyTestCase(unittest.TestCase):
    def test_xmlrpc(self):
        import datetime

        expected = datetime.datetime.now()

        import threading
        thread_1 = threading.Thread(target=xmlrpc_server.run_time_server)
        thread_1.start()

        server_ret_date = xmlrpc_client.connect_server()
        print(server_ret_date)
        actual = datetime.datetime.strptime(server_ret_date, "%Y-%m-%d %H:%M:%S.%f")
        thread_1.join(timeout = 3)

        self.assertEqual(expected.year, actual.year)
        self.assertEqual(expected.month, actual.month)
        self.assertEqual(expected.day, actual.day)

if __name__ == '__main__':
    unittest.main()
