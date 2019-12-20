import unittest
import zeromq_client_send_word as zeromq_client_send_word
import zeromq_server_send_word as zeromq_server_send_word


class MyTestCase(unittest.TestCase):
    def test_zero_mq_send_word(self):
        import datetime

        import threading
        thread_1 = threading.Thread(target=zeromq_server_send_word.run_time_server)
        thread_1.start()

        server_ret_date = zeromq_client_send_word.connect_server()
        thread_1.join()

if __name__ == '__main__':
    unittest.main()
