import logging
import os
import rooms.py

from google.cloud import storage
from flask import (Flask, render_template)

def commentToFile(commentText):
    f= open("comment.csv","w+")

    f.write(commentText + ", ")
    f.close()
    return f


def createComment(roomBucket, commentText):
    f=commentToFile(commentText)
    storage_client = storage.Client()
    room = storage_client.get_bucket(bucket_name)
    room.upload_from_filename(f)

    return

def reply(roomBucket, comment, replyText):
    comment = get_buckets(roomBucket)
    f= open("comment.txt","w")
    f.write(replyText + ",")
    f.close()


    return commentThread
