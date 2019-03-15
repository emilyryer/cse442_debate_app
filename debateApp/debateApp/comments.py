import logging
import os
import rooms
import json

from google.cloud import storage
from flask import (Flask, render_template)

app = Flask(__name__)

def commentToFile(commentText):
    commentThread = {commentText}
    x = json.dumps(commentThread)
    return x


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
