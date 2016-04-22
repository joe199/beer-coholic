#!/usr/bin/env python
# -*- coding: utf-8 -*-

from channels import Channel

import telepot


class DuffmanBot(telepot.Bot):
    """DuffmanBot is my telegram bot"""
    def __init__(self, token):
        super(DuffmanBot, self).__init__(token)
        self.clist = None
        self.chat_id = None

    def set_list(self, clist):
        self.clist = clist

    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            command = msg['text']
            print command
            if self.clist is not None:
                self.clist.append(command)
                self.chat_id = chat_id

    def respond(self, response):
        if self.chat_id is not None:
            self.sendMessage(self.chat_id, response)



class TelegramChannel(Channel):
    """Channel class, received commands from telegram"""
    def __init__(self, name="TelegramChannel"):
        super(TelegramChannel, self).__init__(name)
        self.bot = DuffmanBot("140959535:AAGhwVwbX2UAnDA8MlzwNYHuVkQYEH1coIg")
        self.prova_nfc= []
        self.bot.set_list(self.prova_nfc)
        self.bot.notifyOnMessage()

    def get_msg(self):
        if self.msg_avail():
            print "adeu"
            return self.prova_nfc.pop(0)

    def msg_avail(self):
        #print "hola"
        return len(self.prova_nfc) > 0

    def respond(self, response):
        if response is None:
            response = "Command not understood"
        self.bot.respond(response)
