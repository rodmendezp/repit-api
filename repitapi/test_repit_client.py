import unittest
from unittest import TestCase
from repitapi.client import RepitClient


class TestRepitClient(TestCase):
    def setUp(self):
        self.client = RepitClient().twitch_data
        super().setUp()

    def test_add_twitch_user(self):
        self.client.twitch_user.post_object({'name': 'raidrix', 'twid': 12345})


if __name__ == '__main__':
    unittest.main()
