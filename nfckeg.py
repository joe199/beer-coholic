#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import sys
import subprocess
import time

#import --- nom de les funcions--
import actions as act

class NFCKEG(object):
    """Class for NFCKEG """
    def __init__(self):
        super(NFCKEG, self).__init__()
        #crear lo primordial
        self.actions = []
        self.actions.append(act.telegram)
        self.actions.append(act.nfc)

        self.cl = CommandList() #sensor simulat en una llista


    def entry(self):
        #if entry is telegram:
            #return telegram
        #elseif is nfc:
            #return nfc
        #else:
            #return None
        try:
            return self.cl.next()
        except:
            return (None)

    def next_command(self, list1):
        words = list1.split()
        first_word = words[0]
        rest_words = words[1:]
        response = None
        for entry in self.actions:
            if entry.is_for_you(first_word):
                response = entry.do(rest_words)
        else:
            print "command not found"
        return response


    def mainloop(self):
        while True:
            entry = self.entry()
            if entry:
                response = self.next_command(entry)
                chan.response(response)

            #if entry is telegram:
                #self.act.telegram
            #elseif entry is nfc:
                #self.act.nfc



if __name__ == '__main__':
    print "Starting drinking contest"
    program = NFCKEG()
    program.mainloop()
