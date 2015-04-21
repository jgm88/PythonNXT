#!/usr/bin/env python

import nxt.bluesock
from nxt.motor import *
import time

def connect(idmac):
    b = nxt.bluesock.BlueSock(idmac).connect()
    return b


if __name__=='__main__':

    brick= connect('00:16:53:09:46:3B')

    bPadre = Motor(brick, PORT_B)
    bHijo = Motor(brick, PORT_C)
    sync = SynchronizedMotors(bPadre, bHijo, 0)
    
    current_time = time.time()
    sync.run(100)
    while (time.time() - current_time < 3.0):
        print "Tacho: ", sync.get_tacho()
    sync.brake()