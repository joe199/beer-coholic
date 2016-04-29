#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Action(object):
    """docstring for command"""
    def __init__(self, database, databasec):
        super(Action, self).__init__()
        #self.arg = arg
        self.database= database
        self.beer_quantity = databasec
