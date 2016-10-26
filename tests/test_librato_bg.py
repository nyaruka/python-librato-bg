from __future__ import unicode_literals

import librato
import os
import unittest

from librato_bg import Client
from mock import patch


class MockConnection(object):
    def __init__(self, items):
        self.items = items

    class Queue(object):
        def __init__(self, items):
            self.items = items

        def add(self, name, value, source):
            self.items.append({'name': name, 'value': value, 'source': source})

        def submit(self):
            pass

    def new_queue(self):
        print("new_queue")
        return MockConnection.Queue(self.items)


class TestClient(unittest.TestCase):
    def setUp(self):
        super(TestClient, self).setUp()

        self.mock_queue = []
        with patch.object(librato, 'connect') as mock_connect:
            mock_connect.return_value = MockConnection(self.mock_queue)
            self.client = Client('test-user', '1234567890', debug=True)

    def test_gauge(self):
        self.client.gauge('librato_bg.test', 105, 'lagom')
        self.client.flush()

        self.assertEqual(self.mock_queue, [{'name': 'librato_bg.test', 'source': 'lagom', 'value': 105}])


if __name__ == '__main__':
    """
    We can also test against a real Librato account
    """
    user = os.environ.get('LIBRATO_USER')
    token = os.environ.get('LIBRATO_TOKEN')

    assert user and token, "Must set LIBRATO_USER and LIBRATO_TOKEN to run tests"
    client = Client(user, token, debug=True)

    for i in range(1000):
        client.gauge('librato_bg.test', i, 'lagom')
    client.flush()
