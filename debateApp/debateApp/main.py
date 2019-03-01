import logging
import random

from google.cloud import storage
from flask import (Flask, render_template)

client = storage.Client.from_service_account_json('creds.json')
# from django.shortcuts import render
app = Flask(__name__)
logging.basicConfig(filename='create_room.log', level='INFO', format='w')

@app.route('/')
def response():
    # return render('index.html')
    return 'Main page'

@app.route('/create')
def create_room(room_name='test_bucket', topic='foo'):
    rand_num = random.randint(100000, 999999) #generate a random 6 digit number
    new_bucket_name = room_name + '-' + str(rand_num)
    
    for i in range(10): # Try to make the bucket with 10 different random numbers
        if new_bucket_name in client.list_buckets():
            rand_num = random.randint(100000, 999999)
            new_bucket_name = room_name + '-' + str(rand_num)
            continue
        
        logging.info('Attempting to make bucket with name {}'.format(new_bucket_name))
        new_bucket = client.create_bucket(new_bucket_name)
        add_bucket_label(new_bucket_name, 'topic', topic)
        
        logging.info('NEW BUCKET CREATED: {0}\t\tTOPIC: {1}'.format(
                    new_bucket_name, topic))
        return 'NEW BUCKET CREATED: {0}\t\tTOPIC: {1}'.format(
                new_bucket_name, topic)
    
    logging.error('Unable to create room with the name {}'.format(room_name))
    return 'Unable to create room with the name {}'.format(room_name)

def delete_room():
    return

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