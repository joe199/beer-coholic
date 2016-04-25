#!/usr/bin/env python
# -*- coding: utf-8 -*-

import channels as ch

class Notify(object):
    """Notify class"""
    def __init__(self):
        super(Notify, self).__init__()

    def prova(self):
        pass
        
        #print "La prova ha funcionat!"
        #return self.ch.TelegramChannel.get_msg()

    def notify(self, user, message):
        print "Notify"
        #self.ch.TelegramChannel.get_msg

    def broadcast(self, message):
        print "Broadcast"
