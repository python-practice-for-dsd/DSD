import unittest
import redis_client as redis_client
import redis_server as redis_server


class MyTestCase(unittest.TestCase):
    def test_redis_pubsub(self):
        expected = []

        import threading
        thread_1 = threading.Thread(target=redis_server.run_time_server)
        thread_1.start()

        actual = redis_client.connect_server()
        thread_1.join()

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
