from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
import tkinter.ttk as ttk
from tkcolorpicker import askcolor
#Install Pillow with pip install pillow

def draw_profile_pic(name):
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
    img.save(name + '.png')

#Test Cases (Uncomment to run)
draw_profile_pic('A') #case for single letter nickName
draw_profile_pic('BBBB') #case for multiple letter nickname
