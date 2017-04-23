#!/usr/bin/python

import datetime
import Image
import ImageDraw
import ImageFont
import json
import os
from rgbmatrix import Adafruit_RGBmatrix
import time

# Configuration
height = 32
width = 128

# Set up the matrix
m = Adafruit_RGBmatrix(32, 4)

# Set up the font
f = ImageFont.load(os.path.dirname(os.path.realpath(__file__)) + "/helvR14-ISO8859-1.pil")
image       = Image.new("RGB", (width, height))
draw        = ImageDraw.Draw(image)
textColor   = (128, 128, 128)

# Set up the file reader
allowedToRead = False
shouldReadSecond = 10

def loadJson():
	with open(os.path.dirname(os.path.realpath(__file__)) + "/../node/config.json") as dataFile:
		return json.load(dataFile)

config = loadJson()
textColor = (config["common"]["red"], config["common"]["green"], config["common"]["blue"])

while(True):
	now = datetime.datetime.now()
	hour = now.hour % 12
	hour = 12 if (hour == 0) else hour
	timeStr = "{0}:{1}".format(hour, now.strftime("%M"))

	if(now.second % 10 == 0 and allowedToRead):
		config = loadJson()
		textColor = (config["common"]["red"], config["common"]["green"], config["common"]["blue"])
		allowedToRead = False

	if(now.second % 10 != 0):
		allowedToRead = True

	size = f.getsize(timeStr)
	textHeight = size[1]
	textWidth = size[0]
	xText = (width / 2) - (textWidth / 2)
	yText = (height / 2) - (textHeight / 2)

	draw.rectangle((0, 0, width, height), fill=(0, 0, 0))
	draw.text((0, 0), timeStr, font=f, fill=textColor)
	
	m.SetImage(image.im.id, 0, 0)
