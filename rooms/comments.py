import logging
import os
import rooms
import json

from google.cloud import storage


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


def createComment(bucket, commentText, parentComment=None):
    f = commentToFile(commentText)
    storage_client = storage.Client()
    room = storage_client.get_bucket(bucket_name)
    room.upload_from_filename(f)

    return

def reply(roomBucket, comment, replyText):
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
