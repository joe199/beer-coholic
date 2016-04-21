#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3

class DataBase(object):
    """DataBase class"""
    def __init__(self):
        super(Database, self).__init__()
        #create database
        self.conn = sqlite3.connect('usuaris.db')
        self.cursor = conn.cursor()
        self.cursor.execute('DROP TABLE IF EXISTS "DataBase"')
        self.cursor.execute('''CREATE TABLE `DataBase` (
                `id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                `name`	TEXT,
                `tagid`	TEXT,
                `username`	TEXT,
            );
            ''')

        self.conn.close()
        #Base created
        self.db = sqlite3.connect('usuaris.db')
        self.db.row_factory = sqlite3.Row
        self.cur = self.db.cursor()

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
