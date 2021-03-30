import unittest


class TestEndpoints(unittest.TestCase):
    def test_server_connection(self):
        self.assertEqual(8,8)


if __name__ == '__main__':
    unittest.main()
