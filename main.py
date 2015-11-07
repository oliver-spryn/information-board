#!/usr/bin/python

from business.factories.FirebaseFactory import FirebaseFactory
from business.factories.LogentryFactory import LogentryFactory

fbf = FirebaseFactory()
le = LogentryFactory(fbf)
le.debug("HI")
