import sqlite3


connection = sqlite3.connect('usuaris.db')
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS "DataBase"')
cursor.execute('''CREATE TABLE `DataBase` (
    `id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    `name`	TEXT,
    `tagid`	TEXT,
    `username`	INTEGER NOT NULL,
);
''')

connection.close()
