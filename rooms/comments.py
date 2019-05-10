import logging
import os
import rooms
import json

from google.cloud import storage

# client = storage.Client.from_service_account_json('creds.json')
# logging.basicConfig(filename='comments.log', level='INFO', format='w')

def create_comment_trees(room):
    base_comments = open(x, 'base_trees.txt').close()
    room.upload_from_file('base_comments')
    logging.info('Created base comment tracking file')


def upload_blob(bucket_name='default-unknown', comment='test', destination_blob_name='test-comment'):
    """Uploads a blob to the bucket."""
    storage_client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_string(comment)

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


def createComment(bucket, commentText):
    storage_client = storage.Client()
    last_base = ''
    last_base_int = 0
    with open('base_trees.txt', 'r') as f:
        for line in f:
            if line != '':
                last_base = line
    if last_base != '':
        last_base  = last_base[4:] #remove the word base
        last_base_int = int(last_base)
    new_base = 'base' + str(last_base_int + 1)
    f = open('base_trees.txt', 'a')
    f.write(new_base  + '\n')
    f.close()
    # room = storage_client.get_bucket(bucket_name)
    # room.upload_from_filename(f)

def reply(roomBucket, comment, replyText):
    # with open('base_trees', 'r+') as f:
        # for line in f:
    storage_client = storage.Client()
    commentRoom = storage_client.get_buckets(roomBucket)
    blob = commentRoom.blob(comment)
    thread = json.loads(blob)
    thread.append(replyText)
    json.dumps(thread)

    return commentThread


def deleteComment(roomBucket, comment, replyText):
    storage_client = storage.Client()
    commentRoom = storage_client.get_buckets(roomBucket)
    blob = commentRoom.blob(comment)
    thread = json.loads(blob)
    thread.pop(0)
    json.dumps(thread)

    return commentThread
