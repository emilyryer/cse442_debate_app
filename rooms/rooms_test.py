import rooms
import pytest
from google.cloud import (storage, exceptions)

client = storage.Client.from_service_account_json('creds.json')

def test_create_room():
    retVal = rooms.create_room(room_name='Test Room', topic='test', user='unknown')
    assert retVal == 'NEW BUCKET CREATED: Test Room\nOWNER: unknown\nTOPIC: test'

#def test_join_room():
#    room = client.lookup_bucket('Test Room')
#    labels = room.labels
#    join_code = labels[1]
#    joined_room = rooms.join_room('Test Room', join_code)
#    assert joined_room == room

#def test_delete_room():
#    rooms.delete_room('Test Room')
#    assert client.lookup_bucket(new_bucket_name) == None
