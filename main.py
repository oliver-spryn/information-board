#!/usr/bin/python

import os

dir = next(os.walk("./plugins"))[1]

for name in dir:
	print(name)
