#!/usr/bin/env python

import nxt.bluesock
from nxt.motor import *
import time
import msvcrt


def connect(idmac):

    m = nxt.locator.Method(False, True, False, False)
    b = nxt.bluesock.BlueSock(idmac).connect()
    return b

class mission1_3:
	def __init__(self):
		# vector de estados, [mov+,mov-] para saber en que direccion acelerar
		self.vState = [False, False]
		self.power = 60
		self.dadMotor = None	
		self.sonMotor = None
		self.syncMotor = None
		self.arm = None

	def move(self, direction):

		# vState[0] mov+ vState[1] mov-	

		# Yendo hacia atras y quiero seguir hacia atras
		if(direction == -1 and self.vState[1]):
			return		
		# Yendo hacia adelante y quiero seguir hacia delante
		elif(direction == 1 and self.vState[0]):
			return

		if(direction == 1):
			self.vState[0] = True
			self.vState[1] = False
		else:
			self.vState[0] = False
			self.vState[1] = True

		# Yendo hacia atras y quiero ir hacia delante
		if(direction == 1 and self.vState[1]):
			direction = -1

		self.power *= direction
		
		self.syncMotor.brake()
		self.syncMotor.run(self.power)

	# Dependiendo de la direccion, acelera o decelera
	def speed(self, direction):

		if(self.vState[0]):
			if(self.power < 120 and self.power > 0):
				self.power = self.power + 10 * direction
		elif(self.vState[1]):
			if(self.power < 0 and self.power > -120):
				self.power = self.power - 10 * direction
		else:
			return
		self.syncMotor.run(self.power)

	def turn(self, direction):

		# self.vState[0] = self.vState[1] = False
		# self.syncMotor.brake()
		# self.dadMotor.turn(direction * 100, 180)
		# self.sonMotor.turn(direction * -100, 180)

		if(self.vState[1]):
			self.dadMotor.turn(direction * -100, 180)
			self.sonMotor.turn(direction * 100, 180)
		else:
			self.dadMotor.turn(direction * 100, 180)
			self.sonMotor.turn(direction * -100, 180)	

	def run(self, brick):
		
		self.dadMotor = Motor(brick, PORT_B)
		self.sonMotor = Motor(brick, PORT_C)
		self.syncMotor = SynchronizedMotors(self.dadMotor, self.sonMotor, 0)	

		self.arm = Motor(brick, PORT_A)	

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
					self.move(1)
				elif(key == 's'):
					self.move(-1)

				# Girar a la derecha
				elif(key == 'a'):
					self.turn(1)
				# Girar a la izquierda
				elif(key == 'd'):
					self.turn(-1)

				# Brazo arriba
				elif(key == 'q'):				
					self.arm.reset_position(True)
					self.arm.turn(20, 50)

				# Brazo abajo
				elif(key == 'e'):	
					self.arm.reset_position(True)		
					self.arm.turn(-20, 50)

				# Parar o activar motor
				elif(key == ' '):
					if(self.vState[0] or self.vState[1]):
						self.vState[0] = self.vState[1] = False
						self.syncMotor.brake()
					else:
						self.vState[0] = True
						self.power = 60
						self.syncMotor.run(self.power)	

				#Cerrar programa
				elif(key == 'p'):
					self.syncMotor.brake()
					self.arm.brake()
					break

				# Acelerar
				elif(key == '+'):
					self.speed(1)

				elif(key == '-'):
					self.speed(-1)
	    	
if __name__=='__main__':    
	
	brick = connect('00:16:53:09:46:3B')
	mission = mission1_3()
	mission.run(brick)