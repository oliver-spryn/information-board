#!/usr/bin/env python
from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import os
import time

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat-pwm'  # If you have an Adafruit HAT: 'adafruit-hat'

matrix = RGBMatrix(options = options)

# Draw on the canvas
canvas = matrix.CreateFrameCanvas()
color = graphics.Color(255, 255, 0)

font = graphics.Font()
font.LoadFont(os.path.dirname(os.path.realpath(__file__)) + "/7x13.bdf")

pos = canvas.width

while True:
	canvas.Clear()
	len = graphics.DrawText(canvas, font, 5, 5, color, "Hello World")

	pos -= 1

	if(pos + len < 0):
		pos = canvas.width

	time.sleep(0.05)
	canvas = matrix.SwapOnVSync(canvas)
