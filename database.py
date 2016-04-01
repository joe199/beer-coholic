import sys
import socket
import sys
import os
import subprocess
import time
import threading
import database

class database:

    def __init__(self):
        self.clients = dict()

    def client(self, client, beer):
        if client in self.clients:
            self.clients[client] = self.clients[client] + beer
        else:
            self.clients[client] = beer
        print self.clients
        return self.clients[client]


    def tank(self, tank):
        self.tanki = tank
        tank = float(tank)-0.33
        tank = '%.2f' % (tank)
        return tank

"He afegit comentari per aveure si puc fer un sol comit d'ixo"
if a==b:
    print hola
