# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:10:30 2019

@author: Himanshu Rathore
"""
from PIL import Image

image_name = input("Enter image name: ")

image = Image.open(image_name+".jpg")

# GreyScale mode conversion
GreyScale_image = image.convert('L')
GreyScale_image.save("GreyScale_Sample.jpg")


# Rotating of image by 90 CLKwise
Rotated_90_CLKwise_image = image.transpose(Image.ROTATE_270)
Rotated_90_CLKwise_image.save("Rotated_90_sample.jpg")


# Croping image 
# finding actual width and height of image
width, height = image.size
new_width = 160
new_height = 204
# for centering 
left = (width - new_width)/2
top = (height - new_height)/2
right = (width + new_width)/2
bottom = (height + new_height)/2
# croping
Croped_image = image.crop(box=(left, top, right, bottom))
Croped_image.save("Croped_sample.jpg")


# Creating Thumbnail
image.thumbnail((75,75))
image.save("Thumbnail_sample.jpg")