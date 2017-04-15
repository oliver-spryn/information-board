#!/usr/bin/python

import datetime
import Image
import ImageDraw
import ImageFont
import os
from rgbmatrix import Adafruit_RGBmatrix
import time

# Config
onHour = 8
onMinute = 0

offHour = 22
offMinute = 0

# Set up the matrix
m = Adafruit_RGBmatrix(32, 1)

# Set up the font
f = ImageFont.load(os.path.dirname(os.path.realpath(__file__)) + "/helvR08.pil")
fontYoffset = -2  # Scoot up a couple lines so descenders aren't cropped
image       = Image.new("RGB", (32, 32))
draw        = ImageDraw.Draw(image)
noTimesColor   = (  0,   0, 255) # No predictions = blue

while(True):
	now = datetime.datetime.now()
	draw.rectangle((0, 0, 32, 32), fill=(0, 0, 0))

	if(now.hour >= onHour and now.hour < offHour):
		if((now.hour >= 10 and now.hour <= 12) or (now.hour >= 22 and now.hour <= 23)):
			draw.text((4, 4 + fontYoffset + 8), "{0}:{1}".format(now.hour % 12, now.strftime("%M")), font=f, fill=noTimesColor)
		else:
			draw.text((1, 4 + fontYoffset + 8), "{0}:{1}:{2}".format(now.hour % 12, now.strftime("%M"), now.strftime("%S")), font=f, fill=noTimesColor)

	m.SetImage(image.im.id, 0, 0)
