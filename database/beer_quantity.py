#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_declarative import User, Base
import sqlite3

class beer_quantity(object):
    """DataBase of quantity beer served class"""
    def __init__(self):
        super(beer_quantity, self).__init__()
        try:
            self.conn = sqlite3.connect('usuaris.db')
            self.cursor = self.conn.cursor()
            self.cursor.execute('DROP TABLE IF EXISTS "beer_quantity"'
            return
        except:
            print "la taula de quantitats sera creada"

        #create database
        self.conn = sqlite3.connect('usuaris.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('DROP TABLE IF EXISTS "beer_quantity"')
        self.cursor.execute('''CREATE TABLE beer_quantity (
            `id`	INTEGER NOT NULL PRIMARY KEY,
            `quanity`	INTEGER NOT NULL)''')
        self.conn.close()
        #Base created

        self.db = sqlite3.connect('usuaris.db')
        #self.db.row_factory = sqlite3.Row
        #self.cur = self.db.cursor()

        #mostrar nova base de dades am valors inicials
        a = self.db.execute('select * from beer_quantity')
        data = [row for row in a]
        print "Initial database:"
        for line in data:
            #pass
            print line


    def add(self, user, quantity):
        self.db.execute('INSERT INTO beer_quantity (id, quantity)' +
                         'VALUES (?, ?)',
                         (user, quantity))
        self.db.commit()


    def search(self, columna, fila):
        if columna == "id":
            user =self.db.execute("SELECT * FROM DataBase where id=:Id",
                                    {"Id":fila})
        elif columna == "quantity":
            user =self.db.execute("SELECT * FROM DataBase where username=:Id",
                                    {"Id":fila})
        else:
            user = "ERROR"

        data = [row for row in user]
        print data

        return data


    def beer(self, name):
        return 1.0
