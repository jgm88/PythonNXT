#!/usr/bin/env python

import nxt.bluesock
from nxt.motor import *
import time
import msvcrt

def connect(idmac):

    m = nxt.locator.Method(False, True, False, False)
    b = nxt.bluesock.BlueSock(idmac).connect()
    return b

def run(brick):

	isOn = False

	# minux max key power+=10
	power= 50

	sync = SynchronizedMotors(Motor(brick, PORT_B),Motor(brick, PORT_C))
	arm= Motor(brick, PORT_A)
	
# hacer vector de estados, [mov+,mov-,stop] para saber en que direccion acelerar
# cuando se da + o - 

# funcion motor.idle, para pero tambien desincroniza

while True:
	if msvcrt.kbhit():
		key = msvcrt.getch()
		if(key == 'w'):
			isOn = True
			sync.run(power, True)
		elif(key == 's'):
			isOn = True
			sync.run(power*-1, True)
		elif(key == ' '):
			if(isOn):
				sync.run(0, True)
			else:
				sync.run(power, True)	
		else:
			print "Trolling"

		#elif(key == '+'):			
		#elif(key == '-'):
    	
if __name__=='__main__':
    brick= connect('00:16:53:09:46:3B')
    run(brick)