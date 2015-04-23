#!/usr/bin/env python

from nxt.sensor import *
from nxt.motor import *
import nxt.bluesock
import time
import math

class Robot:

    def __init__(self, brick, tam_encoder=360, wheel_diameter=5.6):
        
        self.brick_= brick
        self.separationBetweenWheels_= 8
        self.syncMotor_ = SynchronizedMotors(Motor(self.brick_, PORT_B), Motor(self.brick_, PORT_C), 0)
        self.cuenta_= ((encoder_*math.pi)/wheelDiameter_)
        self.sensorTouch_= Touch(self.brick, PORT_1)
        self.arm= Motor(self.brick_, PORT_A)

        # 1. Calculamos las cuentas que tendra que pasar para girar hacia un stolado.
        # Si suponemos que un giro sobre si mismo es de de radio separationBewteenWheels, un giro solo ocupara una
        # cuarta parte del perimetro de la circunferencia.
        turn_perimeter = (math.pi * self.wheelDiameter_) / 4
        self.cuentasGiro_ = turn_perimeter / self.cuenta_

    def mision(self):

        print "Espero sensor de choque"
        while self.sensorTouch_.is_pressed() == False: 
            pass;  

        self.syncMotor_.run(70)

        while self.sensorTouch_.is_pressed() == True: 
            pass;  


        # 2. Esperamos durante 2 segundos contactos
        print "Recolecto samples"
        samples= 0
        current_time= time.time()

        # Con estos semaforos nos aseguramos recolectar los samples correctos
        puedoRecolectar = False
        puedoSerPulsado = True

        while (time.time() - current_time)<2.0:                
            if(puedoSerPulsado and self.sensorTouch_.is_pressed()):
                puedoRecolectar = True
                puedoSerPulsado = False
            if(puedoRecolectar):
                puedoRecolectar = False
                samples+=1
            if(self.sensorTouch_.is_pressed() == False):
                puedoSerPulsado = True

        print "Samples recogidos: ",samples
        self.syncMotor_.brake()


        # 1. Giro 45 y continuar recto
        if(samples == 1):
            self.syncMotor_.leader.weak_turn(80, self.cuentasGiro_/2)
            self.syncMotor_.run(70)
        # 2. Giro 90 sentido contrario y continuar
        elif(samples == 2):
            self.syncMotor_.leader.weak_turn(-80, self.cuentasGiro_)
            self.syncMotor_.run(70)
        # 3. Giro 180 y continuar
        elif(samples == 3):
            self.syncMotor_.leader.weak_turn(80, self.cuentasGiro_*2)
            self.syncMotor_.run(70)
        # 4. Detener robot y mover brazo de arriba a abajo 2 veces
        elif(samples == 4):
            self.syncMotor_.brake()

            self.arm.reset_position(True)
            self.arm.turn(20, 50)
            self.arm.reset_position(True)        
            self.arm.turn(-20, 50)

            self.arm.reset_position(True)
            self.arm.turn(20, 50)
            self.arm.reset_position(True)        
            self.arm.turn(-20, 50)

        while True:            
            if msvcrt.kbhit():
                key = msvcrt.getch()
                if(key == "p"):
                    print "PARO"
                    break; 
        
        self.syncMotor_.brake()
        self.syncMotor_.idle()


        self.brick_.play_tone_and_wait(659, 500)

if __name__=='__main__':
    #robot= Robot(nxt.locator.find_one_brick())
    robot= Robot(nxt.bluesock.BlueSock('00:16:53:09:46:3B').connect())
    robot.mision()