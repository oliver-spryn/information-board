#!/usr/bin/python

from business.factories.FirebaseFactory import FirebaseFactory

fbf = FirebaseFactory("https://information-board.firebaseio.com/")
print(fbf.get("/plugins", None))
