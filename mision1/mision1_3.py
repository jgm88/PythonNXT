#!/usr/bin/env python

import nxt.bluesock
from nxt.motor import *
import time
import msvcrt
import math

def connect(mode, mac):
    if(mode=="Usb"):
        return nxt.locator.find_one_brick()
    else:
        return nxt.bluesock.BlueSock(mac).connect()

# brick = connect('00:16:53:09:46:3B')

class Robot:
	
	def __init__(self, brick, tam_encoder=360, wheel_diameter=5.6):
		# vector de estados, [mov+,mov-] para saber en que direccion acelerar
		self.vState = [False, False]
		self.power = 60
		self.separationBetweenWheels_ = 13
		self.syncMotor = SynchronizedMotors(Motor(brick, PORT_B),  Motor(brick, PORT_C), 0)
		self.arm =  Motor(brick, PORT_A)	
		
		self.cuenta_= ((wheel_diameter*math.pi)/tam_encoder)

        # 1. Calculamos las cuentas que tendra que pasar para girar hacia un stolado.
        # Si suponemos que un giro sobre si mismo es de de radio separationBewteenWheels, un giro solo ocupara una
        # cuarta parte del perimetro de la circunferencia.
		self.turn_perimeter = (math.pi * 2.0 * self.separationBetweenWheels_) / 4.0
		self.cuentasGiro_ = self.turn_perimeter / self.cuenta_


	def move(self, direction):

		# vState[0] mov+ vState[1] mov-	

		if(direction == 1):
			if(not self.vState[0] and not self.vState[1]):
				self.power = 60
			if(self.vState[1]):
				self.power *= -1		

			self.vState[0] = True
			self.vState[1] = False

		if(direction == -1):
			if(not self.vState[0] and not self.vState[1]):
				self.power = -60
			if(self.vState[0]):	
				self.power *= direction


			self.vState[0] = False
			self.vState[1] = True
		
		self.syncMotor.brake()
		self.syncMotor.run(self.power)

	# Dependiendo de la direccion, acelera o decelera
	def speed(self, direction):

		if(self.vState[0]):	
			if(self.power < 120 and self.power > 0):
				self.power = self.power + 5 * direction
		elif(self.vState[1]):
			if(self.power < 0 and self.power > -120):
				self.power = self.power - 5 * direction
		else:
			return
		self.syncMotor.brake()
		self.syncMotor.run(self.power)

	def turn(self, direction):

		if(direction == 1):
			self.syncMotor.leader.weak_turn(80, self.cuentasGiro_)
		else:
			self.syncMotor.follower.weak_turn(80, self.cuentasGiro_)

	def stop(self):
		if(self.vState[0] or self.vState[1]):
			self.vState[0] = self.vState[1] = False
			self.syncMotor.brake()
		else:
			self.vState[0] = True
			self.power = 60
			self.syncMotor.run(self.power)	
