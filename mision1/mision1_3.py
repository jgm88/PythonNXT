#!/usr/bin/env python

import nxt.bluesock
from nxt.motor import *
import time

def connect(idmac):

    m = nxt.locator.Method(False, True, False, False)
    b = nxt.bluesock.BlueSock(idmac).connect()
    return b

def run(brick):

	# minux max key power+=10
	power= 50

	sync = SynchronizedMotors(Motor(brick, PORT_B),Motor(brick, PORT_C))
	arm= Motor(brick, PORT_A)
	# keyup
	sync.run(power, True)

	# keydown
	sync.run(power*-1, True)	

	# Rigth

	# Left





if __name__=='__main__':
    brick= connect('00:16:53:09:46:3B')
    run(brick)