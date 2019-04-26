from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
import tkinter.ttk as ttk
from tkcolorpicker import askcolor
#from google.cloud import storage
#Install Pillow with pip install pillow

def draw_profile_pic(name, email):
    initial = ''
    if len(name) == 1:
        initial = name
    else:
        initial = name[0]

    root = tk.Tk()
    style = ttk.Style(root)
    style.theme_use('clam')

    colorTuple = askcolor((255, 255, 0), root)
    colorString = "{}".format(colorTuple[0])
    colorList = colorString.split(", ")
    red=colorList[0].strip('(')
    green=colorList[1]
    blue=colorList[2].strip(')')

    redInt = int(red)
    greenInt = int(green)
    blueInt = int(blue)

    img = Image.new('RGB', (500, 500), color = (redInt, greenInt, blueInt))

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("fonts/DODGE.ttf", 400)
    textRGB = 0
    if (redInt + greenInt + blueInt) < 450:
        textRGB = 255
    draw.text((120,40),initial,(textRGB,textRGB,textRGB),font=font)
    emailFilename = email.replace('.', '')
    emailFilename = emailFilename.replace('@', '')
    filename = emailFilename + '.jpg'
    img.save(filename)
    return filename

def profile_picture_to_bucket(filename):
    storage_client = storage.Client()
    bucket_name = 'debate_app_profile_pics'
    bucket = storage_client.get_bucket(bucket_name)
    bucket.upload_from_filename(filename)

def get_profile_pic(email):
    storage_client = storage.Client()
    emailFilename = email.replace('.', '')
    emailFilename = emailFilename.replace('@', '')
    bucket_name = 'debate_app_profile_pics'
    bucket = storage_client.get_bucket(bucket_name)
    

#Test Cases (Uncomment to run)
draw_profile_pic('A', 'test@test.com') #case for single letter nickName
draw_profile_pic('BBBB', 'test2@test.com') #case for multiple letter nickname
