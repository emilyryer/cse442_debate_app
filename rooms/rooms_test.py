import unittest
import logging
import rooms

from google.cloud import storage

client = storage.Client.from_service_account_json('creds.json')
logging.basicConfig(filename='test_room.log', level='INFO', format='w')

class TestRooms(unittest.TestCase):

	def test_add_label(self):
		logging.info('Starting label test')
		buckets = client.list_buckets(prefix='label-test')
		try:
			bucket =
		except Exception as e:
			raise e
		create_room('label-test', 'testing the label maker')

if __name__ == '__main__':
    unittest.main()
