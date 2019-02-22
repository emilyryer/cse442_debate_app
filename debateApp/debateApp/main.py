import logging
import os

from google.cloud import storage
from flask import Flask

client = storage.Client.from_service_account_json('creds.json')
app = Flask(__name__)

@app.route('/')
def create_room(room_name='test_bucket'):
    new_room = client.create_bucket('debate-app-' + room_name)
    return 'Created new room in bucket {}'.format(room_name)

def get_buckets(room_name):
    return

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