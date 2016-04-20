#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import sys
import subprocess
import time

#import --- nom de les funcions--
from commandlist import CommandList
<<<<<<< HEAD
from actions import actions as act
from channels import channels as ch
=======
import actions as act
import channels as ch
>>>>>>> 7e8575c944480e0ec44656e87511cee38e1bd320



class NFCKEG(object):
    """Class for NFCKEG """
    def __init__(self):
        super(NFCKEG, self).__init__()
        #crear lo primordial
        self.actions = []
        self.actions.append(act.telegram())
        self.actions.append(act.nfc())

        self.cl = CommandList() #sensor simulat en una llista

        self.channels = []
        self.channels.append(ch.TextChannel())


    def entry(self):
        try:
            return self.cl.next()
        except:
            return (None, None)

    def next_command(self, list1):
        words = list1.split()
        first_word = words[0]
        rest_words = words[1:]
        response = None
        for ha in self.actions:
            if ha.is_for_you(first_word):
                response = ha.do(rest_words)
        else:
            print "command not found"
        return response

    def update_channels(self):
            for chan in self.channels:
                while chan.msg_avail():
                    self.cl.append((chan, chan.get_msg()))

    def mainloop(self):
        while True:
            (chan, entry) = self.entry()
            if entry:
                print entry, "valor de entry"
                response = self.next_command(entry)
                chan.response(response)
            time.sleep(1)
            self.update_channels()

            #if entry is telegram:
                #self.act.telegram
            #elseif entry is nfc:
                #self.act.nfc



if __name__ == '__main__':
    print "Starting drinking contest"
    program = NFCKEG()
    program.mainloop()
