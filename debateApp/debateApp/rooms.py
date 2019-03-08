import logging
import random

from google.cloud import (storage, exceptions)
from flask import (Flask, render_template)

client = storage.Client.from_service_account_json('creds.json')
# from django.shortcuts import render
app = Flask(__name__)
logging.basicConfig(filename='room.log', level='INFO', format='w')

@app.route('/')
def response():
    # return render('index.html')
    return 'Main page'

@app.route('/create')
def create_room(room_name='default', topic='', user='unknown'):
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

    logging.info('NEW BUCKET CREATED: {0}\nOWNER: {1}\nTOPIC: {2}'.format(
                new_bucket_name, user, topic))
    return 'NEW BUCKET CREATED: {0}\nOWNER: {1}\nTOPIC: {2}'.format(
                new_bucket_name, user, topic)

@app.route('/delete')
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


@app.errorhandler(500)
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
