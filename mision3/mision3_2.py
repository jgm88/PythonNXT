#!/usr/bin/env python

import nxt.bluesock
from nxt.sensor import *
from nxt.motor import *
import time
import math

class Robot:

    def __init__(self, brick, tam_encoder=360, wheel_diameter=5.6):

        self.brick_= brick
        self.separationBetweenWheels_= 14
        self.syncMotor_ = SynchronizedMotors(Motor(self.brick_, PORT_B), Motor(self.brick_, PORT_C), 0)
        self.sensorLight_= Light(brick, PORT_3)
        self.sensorLight_.set_illuminated(True)
        self.cuenta_= ((wheel_diameter*math.pi)/tam_encoder)

        # 1. Calculamos las cuentas que tendra que pasar para girar hacia un stolado.
        # Si suponemos que un giro sobre si mismo es de de radio separationBewteenWheels, un giro solo ocupara una
        # cuarta parte del perimetro de la circunferencia.
        turn_perimeter = (math.pi * 2.0 * self.separationBetweenWheels_) / 4.0
        self.cuentasGiro_ = turn_perimeter / self.cuenta_


    def giro(self):

        print "Voi a girar perra"
        self.syncMotor_.leader.weak_turn(60, self.cuentasGiro_)
        self.syncMotor_.follower.weak_turn(-60, self.cuentasGiro_)
        time.sleep(4)

    def mision(self):

        #while True:
        #     print "Sample: " ,self.sensorLight_.get_lightness()

        print "Inicia mision"
        num_line_max=1
        while (num_line_max<4):
          
            # 1.Mover hasta siguiente linea negra establecida por parametro
            self.syncMotor_.run(65)
            lines_passed=0
            puedoRecolectar=False
            puedoSerPulsado=True
            
            while True:
                if(puedoSerPulsado and self.sensorLight_.get_lightness()>=400):
                    puedoRecolectar = True
                    puedoSerPulsado = False
                if(puedoRecolectar):
                    puedoRecolectar = False
                    lines_passed+=1
                    print "Lines passed ida: ", lines_passed
                if(self.sensorLight_.get_lightness()<400):
                    puedoSerPulsado = True

                if(num_line_max==lines_passed):
                    break;

            self.syncMotor_.brake()
            time.sleep(1)
            self.giro()
            self.syncMotor_.run(65)
            
            while True:
                if(puedoSerPulsado and self.sensorLight_.get_lightness()>=400):
                    puedoRecolectar = True
                    puedoSerPulsado = False
                if(puedoRecolectar):
                    puedoRecolectar = False
                    lines_passed-=1
                    print "Lines passed vuelta: ", lines_passed
                if(self.sensorLight_.get_lightness()<400):
                    puedoSerPulsado = True

                if(lines_passed==0):
                    break;

            self.syncMotor_.brake()
            num_line_max+=1
            time.sleep(1)
            self.giro()
        
        # 3. Opcional. Emitir sonido como finalizacion
        self.brick_.play_tone_and_wait(659, 500)

if __name__=='__main__':
    robot= Robot(nxt.locator.find_one_brick())
    #robot= Robot(nxt.bluesock.BlueSock('00:16:53:09:46:3B').connect())
    robot.mision()
