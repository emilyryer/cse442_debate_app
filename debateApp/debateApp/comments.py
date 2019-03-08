import logging
import os
import rooms.py
import json

from google.cloud import storage
from flask import (Flask, render_template)

def commentToFile(commentText):
    commentThread = {commentText}
    x = json.dumps(commentThread)
    return x


def createComment(roomBucket, commentText):
    f=commentToFile(commentText)
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
