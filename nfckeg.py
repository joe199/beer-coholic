import socket
import sys
import os
import subprocess
import time
import threading
import database

beer = 0
tank = 0.99
d = database.database()

class NFCKEG(threading.Thread):

    def __init__(self, client):
        threading.Thread.__init__(self)
        self.client_sock, self.client_addr = client
        
    def run(self):

        global beer
        global tank

        while True:

            #time.sleep(2)
            value = self.client_sock.recv(1024)  
 
            if tank < 0.33:
                    print 'Recharging the tank $$'
                    value2 = 'Whait'
                    self.client_sock.sendall(str(value2))
                    time.sleep(2)
                    tank = 1.65
                    print 'Tank recharged!'
 
            print '\nState 1 of the tank is %s L.' % tank
            tanki = tank
            tank = float(d.tank(tank))
            beer = tanki - tank
            tdrinked = d.client(value, beer)
            print 'State 2 of the tank is %s L.' % tank
            value2 = tdrinked
            self.client_sock.sendall(str(value2))
                                                        
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 9999))
sock.listen(3)
print 'Waiting_for_drinkers_...'

while True:
    client = sock.accept()
    NFCKEG(client).start()
