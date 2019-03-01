import unittest

from main import create_room

client = storage.Client.from_service_account_json('creds.json')

class TestCreateRoom(unittest.TestCase):

	def test_create_no_conflict(self):

		return


if __name__ == '__main__':
    unittest.main()