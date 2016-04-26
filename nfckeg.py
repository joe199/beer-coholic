#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import sys
import subprocess
import time
import yaml

#import --- nom de les funcions--
from commandlist import CommandList
import actions as act
import channels as ch
import database as db
import sensors as sn

class NFCKEG(object):
    """Class for NFCKEG """
    def __init__(self):
        super(NFCKEG, self).__init__()
        #crear lo primordial
        self._get_config()
        self.Datab = db.DataBase()
        self.actions = []
        self.actions.append(act.telegram(self.Datab))
        self.actions.append(act.nfc(self.Datab))



        self.cl = CommandList() #sensor simulat en una llista

        self.channels = []
        self.channels.append(ch.TelegramChannel(self.cfg))
        self.channels.append(ch.TextChannel())

        self.sensors = []
        self.sensors.append(sn.NfcSensor())
        self.sensors.append(sn.FlowSensor())


    def _get_config(self):
        with open("configuration.yaml") as f:
            self.cfg = yaml.load(f)
            self.token = self.cfg["beer-coholic"]["token"]

    def entry(self):
        try:
            return self.cl.next()
        except:
            return (None, None)

    def next_command(self, list1):
        words = list1.split(",")
        chanel = words[0]
        try:
            info1 = words[1]
            info2 = words[2]
        except:
            info1=None
            info2=None
        response = "Command not found"
        for ha in self.actions:
            if ha.is_for_you(chanel):
                response = ha.do(info1, info2)

        return response

    def update_channels(self):
        for chan in self.channels:
            while chan.msg_avail():
                self.cl.append((chan, chan.get_msg()))
                print chan, " ", chan.get_msg


    def mainloop(self):
        while True:
            (chan, entry) = self.entry()
            if entry:
                print "\n*", entry
                response = self.next_command(entry)
                chan.respond(response)
            time.sleep(1)
            self.update_channels()

            #if entry is telegram:
                #self.act.telegram
            #elseif entry is nfc:
                #self.act.nfc



if __name__ == '__main__':
    print "Starting drinking contest:\n"
    program = NFCKEG()
    program.mainloop()
