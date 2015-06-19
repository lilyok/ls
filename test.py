#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading

def f():
    # do something here ...
    # call f() again in 60 seconds
    print 1
    threading.Timer(10, f).start()

# start calling f now and every 60 sec thereafter
f()