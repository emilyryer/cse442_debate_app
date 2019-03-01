import logging
import os
import main.py

from google.cloud import storage
from flask import Flask

commentThread = list

def commentToFile(commentText):
    f= open("comment.txt","w+")
    f.write(commentText)
    return f


def createComment(roomBucket, commentText):
    f=commentToFile(commentText)
    storage_client = storage.Client()
    room = storage_client.get_bucket(bucket_name)
    room.upload_from_filename(f)

    return

def reply(roomBucket, comment, replyText):
    comment = get_buckets(room)

    return commentThread
