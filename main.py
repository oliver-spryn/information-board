#!/usr/bin/python

from business.factories.FirebaseFactory import FirebaseFactory
from business.factories.LogentryFactory import LogentryFactory
from business.foundation.Bootstrapper import Bootstrapper

fbf = FirebaseFactory()
le = LogentryFactory(fbf)

Bootstrapper(fbf, le)
