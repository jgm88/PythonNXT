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
	power= 60

	bPadre = Motor(brick, PORT_B)
	bHijo = Motor(brick, PORT_C)
	sync = SynchronizedMotors(bPadre, bHijo, 0)	

	arm= Motor(brick, PORT_A)
	
# hacer vector de estados, [mov+,mov-,stop] para saber en que direccion acelerar
# cuando se da + o - 

# funcion motor.idle, para pero tambien desincroniza
	print "*Ordenes para el robot:"
	print "	W o S 	avanzar o retroceder"
	print "	A o D 	girar"
	print "	Q o E 	mover el brazo"
	print "	Espacio 	parar"
	print "	+ o - 	acelerar"
	print "	P para salir del programa"

	while True:
		if msvcrt.kbhit():
			key = msvcrt.getch()

			# Movimiento
			if(key == 'w'):
				if(isOn == False):
					isOn = True
					sync.run(power)
			elif(key == 's'):
				if(!isOn):
					isOn = True
					sync.run(power*-1)

			# Girar a la derecha
			elif(key == 'a'):
				isOn = True
				bPadre.turn(100, 180)
				bHijo.turn(-100, 180)

			# Girar a la izquierda
			elif(key == 'd'):
				isOn = True
				bPadre.turn(-100, 180)
				bHijo.turn(100, 180)

			# Brazo arriba
			elif(key == 'q'):				
				arm.reset_position(True)
				arm.turn(20, 50)

			# Brazo abajo
			elif(key == 'e'):	
				arm.reset_position(True)		
				arm.turn(-20, 50)

			# Parar o activar motor
			elif(key == ' '):
				if(isOn):
					isOn = False
					sync.brake()
				else:
					sync.run(power)	

			#Cerrar programa
			elif(key == 'p'):
				sync.brake()
				arm.brake()
				break

			#elif(key == '+'):			
			#elif(key == '-'):
	    	
if __name__=='__main__':
    brick= connect('00:16:53:09:46:3B')
    run(brick)