import logging
import random

from google.cloud import (storage, exceptions)

logging.basicConfig(filename='room.log', level='INFO', format='w')

def create_room(room_name='default', topic='', user='unknown'):
    storage_client = storage.Client()
    if user == '' or user == 'unknown':
        logging.warning('No username given')
    new_bucket_name = room_name + '-' + user

    if client.lookup_bucket(new_bucket_name) != None:
        logging.error('Bucket already exists with name {}'.format(new_bucket_name))
        return 'Bucket already exists with name {}'.format(new_bucket_name)

    logging.info('Attempting to make bucket with name {}'.format(new_bucket_name))
    try:
        new_bucket = client.create_bucket(new_bucket_name)
    except Exception as e:
        return 'Unable to make bucket. Exception occurred: {}'.format(e)

    add_bucket_label(new_bucket_name, 'topic', topic)
    add_bucket_label(new_bucket_name, 'join-code', random.randint(1000, 9999))

    logging.info('NEW BUCKET CREATED: {0}\nOWNER: {1}\nTOPIC: {2}'.format(
                new_bucket_name, user, topic))
    return 'NEW BUCKET CREATED: {0}\nOWNER: {1}\nTOPIC: {2}'.format(
                new_bucket_name, user, topic)

def join_room(room_name, join_code):
    room = client.lookup_bucket(room_name)
    if room == None:
        logging.error('No bucket exists with name {}'.format(room_name))
    labels = room.labels
    if int(join_code) == int(labels[join-code]):
        return room
    logging.error(
        'Incorrect join code given. Was given room {0} with code {1}'.format(
        room_name, join_code))

def delete_room(bucket_name):
    """Deletes a room. The room must be empty."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    bucket.delete()
    logging.info('Bucket {} deleted'.format(bucket.name))

def add_bucket_label(bucket_name, key, value):
    """Add a label to a bucket."""
    bucket = client.get_bucket(bucket_name)

    labels = bucket.labels
    labels[key] = value
    bucket.labels = labels
    logging.info('Added labels to bucket {}.'.format(bucket.name))
    bucket.patch()

    print('Updated labels on {}.'.format(bucket.name))

def upload_blob(bucket_name='default-unknown', comment='test', destination_blob_name='test-comment'):
    """Uploads a blob to the bucket."""
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_string(comment)
    # metadata = {'Owner': 'unknown'}
    # blob.metadata = metadata

    return('String {} uploaded to {}.'.format(
        comment,
        destination_blob_name))

def list_blobs(bucket_name='default-unknown'):
    """Lists all the blobs in the bucket."""
    bucket = client.get_bucket(bucket_name)

    blobs = bucket.list_blobs()

    for blob in blobs:
        # blob.owner = 'unknown'
        blob_metadata(blob)
    return 'All Blobs: {}'.format(blobs)

def blob_metadata(blob):
    """Prints out a blob's metadata."""

    print('Blob: {}'.format(blob.name))
    print('Bucket: {}'.format(blob.bucket.name))
    print('Storage class: {}'.format(blob.storage_class))
    print('ID: {}'.format(blob.id))
    print('Size: {} bytes'.format(blob.size))
    print('Updated: {}'.format(blob.updated))
    print('Generation: {}'.format(blob.generation))
    print('Metageneration: {}'.format(blob.metageneration))
    print('Etag: {}'.format(blob.etag))
    print('Owner: {}'.format(blob.owner))
    print('Component count: {}'.format(blob.component_count))
    print('Crc32c: {}'.format(blob.crc32c))
    print('md5_hash: {}'.format(blob.md5_hash))
    print('Cache-control: {}'.format(blob.cache_control))
    print('Content-type: {}'.format(blob.content_type))
    print('Content-disposition: {}'.format(blob.content_disposition))
    print('Content-encoding: {}'.format(blob.content_encoding))
    print('Content-language: {}'.format(blob.content_language))
    print('Metadata: {}'.format(blob.metadata))
    print("Temporary hold: ",
          'enabled' if blob.temporary_hold else 'disabled')
    print("Event based hold: ",
          'enabled' if blob.event_based_hold else 'disabled')
    if blob.retention_expiration_time:
        print("retentionExpirationTime: {}"
              .format(blob.retention_expiration_time))


def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
