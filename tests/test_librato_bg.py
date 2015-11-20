import unittest
from librato_bg import Client
import os

class TestBGSubmission(unittest.TestCase):

    def setUp(self):
        super(TestBGSubmission, self).setUp()

        user = os.environ.get('LIBRATO_USER')
        token = os.environ.get('LIBRATO_TOKEN')

        assert user and token, "Must set LIBRATO_USER and LIBRATO_TOKEN to run tests"
        self.client = Client(user, token, debug=True)

    def test_foo(self):
        for i in range(1000):
            self.client.track('librato_bg.test', i, 'lagom')
        self.client.flush()

if __name__ == '__main__':
    unittest.main()
