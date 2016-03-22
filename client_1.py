import socket
import struct
import random
import sys
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9999))

value = sys.argv[1]
#if (value != 'BEER'):
#    print "ERR: unknown command"
#    exit(-1)

while True:
    sock.sendall(value)
    print '\nSent', value
    value2 = sock.recv(1024)

    if value2 == 'Whait':
        print 'Recharging the tank, whait a little bit :('
        value2 = sock.recv(1024)

    if value2 != 'Whait':
        print '%s has drunk %s L. of beer' % (value, value2)
    time.sleep(2)

sock.close()


