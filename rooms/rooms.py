import logging
import random
import comments

from google.cloud import (storage, exceptions)

# client = storage.Client.from_service_account_json('creds.json')
logging.basicConfig(filename='rooms.log', level='INFO', format='w')

def create_room(room_name='default', topic='', user='unknown'):
    storage_client = storage.Client()
    if user == '' or user == 'unknown':
        logging.error('No username given')
    new_bucket_name = room_name + '-' + user

    if client.lookup_bucket(new_bucket_name) != None:
        logging.error('Bucket already exists with name {}'.format(new_bucket_name))
        return 'Bucket already exists with name {}'.format(new_bucket_name)

    logging.info('Attempting to make bucket with name {}'.format(new_bucket_name))
    try:
        new_bucket = client.create_bucket(new_bucket_name)
    except Exception as e:
        logging.error('Unable to make bucket. Exception occurred: {}'.format(e))
        return 'Unable to make bucket. Exception occurred: {}'.format(e)

    add_bucket_label(new_bucket_name, 'topic', topic)
    add_bucket_label(new_bucket_name, 'join-code', random.randint(1000, 9999))

    create_room_users(user, new_bucket)
    create_comment_trees(new_bucket)

    logging.info('NEW BUCKET CREATED: {0}\nOWNER: {1}\nTOPIC: {2}'.format(
                new_bucket_name, user, topic))
    return 'NEW BUCKET CREATED: {0}\nOWNER: {1}\nTOPIC: {2}'.format(
                new_bucket_name, user, topic)

def create_room_users(owner, room):
    file = json.dumps(owner + "-OWNER")
    room.upload_from_filename(file)

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
