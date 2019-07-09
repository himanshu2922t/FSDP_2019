# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 15:41:01 2019

@author: Himanshu Rathore

Project Name: Certificate Generator
"""
from PIL import Image, ImageDraw, ImageFont

# Creating Blank Sheet (white background)
#Blank_sheet = Image.new('RGB', (1200,800), (255,255,255))

# Creating Template
Blank_sheet = Image.open('background.png')

# Resizing logo image
logo = Image.open('Forsk_logo_color.png')
basewidth = 200
wpercent = (basewidth/float(logo.width))
relative_height = int((float(logo.height)*float(wpercent)))
logo = logo.resize((basewidth,relative_height) , Image.ANTIALIAS)

# Pasting Logo on Blank Sheet
position = ((Blank_sheet.width-logo.width)//2 , (Blank_sheet.height-logo.height)//2+120)
Blank_sheet.paste(logo, position, logo)
Blank_sheet.save('Temp.png')

# Intiating draw object to write on a existing image
draw = ImageDraw.Draw(Blank_sheet)

# Selecting fonts
name_font = ImageFont.truetype('Fonts\\MeriendaOne-Regular.ttf', size=40)
program_font = ImageFont.truetype('Fonts\\AdobeDevanagari-Bold.otf', size=36)
date_font = ImageFont.truetype('Fonts\\AdobeDevanagari-Regular.otf', size=32)

#input from user
participants = []
program = input("Enter Program Name: ").upper()
date = input("Enter Date: ")
while True:
    name = input("Enter Participant Name: ")
    if not name:
        break
    participants.append(name)
    
# Writing Text on Template
for name in participants:
    draw.text((290,280), program, (37,54,78), font=program_font)
    draw.text((330,320), date, (37,54,78), font=date_font)
    draw.text((200,180), name, (37,54,78), font=program_font)
    Blank_sheet.save("{}.png".format(name))    
    