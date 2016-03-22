import socket
import sys
import os
import subprocess
import time
import threading

beer = 0
tank = 0.99

def AddBeer(beer):
    beer = float(beer)+0.33
    beer = '%.2f' % (beer)
    return beer

def Tank(tank):
    tank = float(tank)-0.33
    tank = '%.2f' % (tank)
    return tank    

class NFCKEG(threading.Thread):

    def __init__(self, client):
        threading.Thread.__init__(self)
        self.client_sock, self.client_addr = client

    def run(self):
        global beer
        global tank

        while True:

            time.sleep(2)
            print '\nState 1 of the tank is %s L.' % tank
            value = self.client_sock.recv(3)
            
            tanki = tank
            tank = float(Tank(tank))
            beer = beer + tanki - tank
            print 'State 2 of the tank is %s L.' % tank
            value2 = 'You have drinked %s L.' % beer
            self.client_sock.sendall(str(value2))

            if tank < 0.33:
                    print 'Recharging the tank $$'
                    value2 = 'Whait'
                    self.client_sock.sendall(str(value2))
                    time.sleep(10)
                    tank = 1.65
                    print 'Tank recharged!'
                                                        
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 9999))
sock.listen(4)
print 'Waiting_for_drinkers_...'

while True:
    client = sock.accept()
    NFCKEG(client).start()
