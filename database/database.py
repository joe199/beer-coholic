#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_declarative import User, Base
import sqlite3

class DataBase(object):
    """DataBase class"""
    def __init__(self):
        super(DataBase, self).__init__()

        #create database
        self.conn = sqlite3.connect('usuaris.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('DROP TABLE IF EXISTS "DataBase"')
        self.cursor.execute('''CREATE TABLE DataBase (
            `id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            `username`	TEXT,
            `tagid`	TEXT,
            `name`	TEXT)''')
        self.conn.close()
        #Base created

        self.db = sqlite3.connect('usuaris.db')
        #self.db.row_factory = sqlite3.Row
        #self.cur = self.db.cursor()

        #add the initials values to the database
        with open("usuaris.txt","r") as f:
            for line in f:
                line=line.strip()
                user = line.split(",")
                username = user[0]
                tagid = user[1]
                name = user[2]
                self.add(name, tagid, username)

        #mostrar nova base de dades am valors inicials
        a = self.db.execute('select * from DataBase')
        data = [row for row in a]
        print "Initial database:"
        for line in data:
            #pass
            print line


    def add(self, name, tagid, username):
        self.db.execute('INSERT INTO DataBase (name, tagid, username)' +
                         'VALUES (?, ?, ?)',
                         (name, tagid, username))
        self.db.commit()


    def search(self, columna, fila):
        if columna == "id":
            user =self.db.execute("SELECT * FROM DataBase where id=:Id",
                                    {"Id":fila})
        elif columna == "username":
            user =self.db.execute("SELECT * FROM DataBase where username=:Id",
                                    {"Id":fila})
        elif columna == "tagid":
            user =self.db.execute("SELECT * FROM DataBase where tagid=:Id",
                                    {"Id":fila})
        elif columna == "name":
            user =self.db.execute("SELECT * FROM DataBase where name=:Id",
                                    {"Id":fila})
        else:
            user = "ERROR"

        data = [row for row in user]
        print data

        return data


    def beer(self, name):
        return 1.0

    def reset(self):
        #create database
        self.conn = sqlite3.connect('usuaris.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('DROP TABLE IF EXISTS "DataBase"')
        self.cursor.execute('''CREATE TABLE DataBase (
            `id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            `username`	TEXT,
            `tagid`	TEXT,
            `name`	TEXT)''')
        self.conn.close()
        #Base created

        #add the initials values to the database
        with open("usuaris.txt","r") as f:
            for line in f:
                user = line.split(",")
                username = user[0]
                tagid = user[1]
                name = user[2]
                self.add(name, tagid, username)

        #mostrar nova base de dades am valors inicials
        a = self.cur.execute('select * from DataBase')
        data = [row for row in a]
        print "Initial database:"
        for line in data:
            pass
            #print line
