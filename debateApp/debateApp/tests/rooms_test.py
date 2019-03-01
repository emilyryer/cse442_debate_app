import unittest
import logging

from google.cloud import storage
from main import create_room

client = storage.Client.from_service_account_json('creds.json')

class TestCreateRoom(unittest.TestCase):
	self.bucket = ''

	def test_create_no_conflict(self):
		create_room('conflict', 'foo')
		return


if __name__ == '__main__':
    unittest.main()