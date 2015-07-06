#!/usr/bin/python

import Image
import ImageDraw
import ImageFont
import os
import time

from business.drivers.rgbmatrix import Adafruit_RGBmatrix
from business.modules.Forecast import Forecast
from business.parse.connection import register
from datetime import datetime
from datetime import timedelta

# Register the Parse library with an account
app = os.environ.get("IB_PARSE_APP_ID")
key = os.environ.get("IB_PARSE_REST_API_KEY")
register(app, key)

# Config
onHour = 8
onMinute = 0

offHour = 22
offMinute = 0

# Get the weather
fore = Forecast()

# Set up the matrix
m = Adafruit_RGBmatrix(32, 1)

# Set up the font
f = ImageFont.load(os.path.dirname(os.path.realpath(__file__)) + "/assets/fonts/helvR08.pil")
fontYoffset = -2  # Scoot up a couple lines so descenders aren't cropped
image       = Image.new("RGB", (32, 32))
draw        = ImageDraw.Draw(image)
noTimesColor   = (  0,   0, 255) # No predictions = blue
refresh = datetime.now() + timedelta(minutes = 10)
do = 0 # 0 = time, 1 = forecast

while(True):
	now = datetime.now()
	draw.rectangle((0, 0, 32, 32), fill=(0, 0, 0))

	if(now.hour >= onHour and now.hour < offHour):
        if do == 0: # Time
            hr = now.hour % 12

            if hr == 0:
                hr = 12

    		if((now.hour >= 10 and now.hour <= 12) or (now.hour >= 22 and now.hour <= 23)):
    			draw.text((4, 4 + fontYoffset + 8), "{0}:{1}".format(hr, now.strftime("%M")), font=f, fill=noTimesColor)
    		else:
    			draw.text((1, 4 + fontYoffset + 8), "{0}:{1}:{2}".format(hr, now.strftime("%M"), now.strftime("%S")), font=f, fill=noTimesColor)
        else: # Forecast
            current = fore.data["currently"]
            today = fore.data["daily"]["data"]["0"]

            draw.text((0, fontYoffset), current["summary"], font = f, fill = noTimesColor)
            draw.text((0, 4 + fontYoffset + 8), "Now: {0}F".format(int(round(current["summary"]))), font = f, fill = noTimesColor)
            draw.text((0, 8 + fontYoffset + 16)) "{0}F - {1}F".format(int(round(today["temperatureMin"])), int(round(today["temperatureMax"])), font = f, fill = noTimesColor)

        if now >= refresh:
            refresh = now + timedelta(minutes = 10)
            do = (do + 1) % 2 # Flip between 0 and 1

            if do == 1:
                fore.refreshData()

	m.SetImage(image.im.id, 0, 0)
