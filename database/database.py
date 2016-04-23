#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

class DataBase(object):
    """DataBase class"""
    def __init__(self):
        super(DataBase, self).__init__()
        #create database
        self.conn = sqlite3.connect('usuaris.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('DROP TABLE IF EXISTS "DataBase"')
        hr = self.cursor.execute('''CREATE TABLE DataBase (
                `id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                `name`	TEXT,
                `tagid`	TEXT,
                `username`	TEXT)''')
        self.conn.close()
        #Base created

        self.db = sqlite3.connect('usuaris.db')
        self.db.row_factory = sqlite3.Row
        self.cur = self.db.cursor()

        with open("usuaris.txt","r") as f:
            for line in f:
                user = line.split(",")
                name = user[0]
                tagid = user[1]
                username = user[2]
                self.add(name, tagid, username)

        a = self.cur.execute('select * from DataBase')
        data = [row for row in a]
        print "Initial database:"
        for line in data:
            #pass
            print line


    def add(self, name, tagid, username):
        self.cur.execute('INSERT INTO DataBase (name, tagid, username)' +
                         'VALUES (?, ?, ?)',
                         (name, tagid, username))
        self.db.commit()


    def search(self, name):
        self.cur.execute('select * from DataBase where name=:name',
                         {"name": name})
        return self.cur.fetchall()

    def beer(self, name):
        return 1.0
