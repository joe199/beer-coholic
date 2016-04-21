#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Channel(object):
    """Channel class"""
    def __init__(self, name):
        super(Channel, self).__init__()
        self.name = name

    def respond(self, response):
        print "Response: ", response
