#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Action(object):
    """docstring for command"""
    def __init__(self):
        super(Action, self).__init__()
        #self.arg = arg
        
class telegram(Action):
    """docstring for telegram"""
    def __init__(self):
        super(telegram, self).__init__()
        self.consult = ["telegram"]

    def is_for_you(self, word):
        if word in self.consult:
            return True
        return False

    def do(self, command):
        return "Telegram Done"


class nfc(Action):
    """client beer updating"""
    def __init__(self):
        super(nfc, self).__init__()
        self.consult = ["nfc"]

    def is_for_you(self, word):
        if word in self.consult:
            return True
        return False

    def do(self, command):
        return "NFC Done"
