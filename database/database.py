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
        #load session
        # Create engine and bind base to it
        path_to_db = "usuaris.db"
        engine = create_engine('sqlite:///' + path_to_db)
        Base.metadata.bind = engine
        # Make a new session and return it
        DBSession = sessionmaker(bind = engine)
        session = DBSession()
        #searching users
        session.query(User).all()

        if columna == "id":
            user = session.query(User).filter_by(id=fila).all()
        elif columna == "username":
            user = session.query(User).filter_by(username=fila).all()
        elif columna == "tagid":
            user = session.query(User).filter_by(tagid=fila).all()
        elif columna == "name":
            user = session.query(User).filter_by(name=fila).all()
        else:
            user = "ERROR"
        print user

        return user


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
