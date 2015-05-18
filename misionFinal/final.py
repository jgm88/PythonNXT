#!/usr/bin/env python

import nxt.bluesock
import nxt.locator
from nxt.sensor import *
from nxt.motor import *
import time
import math

class Robot:

    def __init__(self, brick, tam_encoder=360, wheel_diameter=5.6):

        self.anchoCoche = 20 #medida coche
        self.largoCoche = 22
        self.brick_= brick
        self.syncMotor_ = SynchronizedMotors(Motor(self.brick_, PORT_B), Motor(self.brick_, PORT_C), 0)
        self.arm_ = Motor(self.brick_, PORT_A)
        self.sensorUltraSound_= Ultrasonic(self.brick_, PORT_1)

        self.separationBetweenWheels_= 14
        self.cuenta_= ((wheel_diameter*math.pi)/tam_encoder)
        turn_perimeter = (math.pi * 2.0 * self.separationBetweenWheels_) / 4.0
        self.cuentasGiro_ = turn_perimeter / self.cuenta_
        self.cuentasTamLargo_ = self.largoCoche / self.cuenta_

        self.sensorUltraSound_.command(0x02) 

    def mision(self):

        #1. Ir en linea recta hasta encontrar un objeto
        print "Buscanco Hueco"
        self.syncMotor_.run(70)

        while self.sensorUltraSound_.get_distance() < self.anchoCoche: #medida del robot
            print self.sensorUltraSound_.get_distance()
            pass
        print "Hueco Detectado"
        #recorrido total + largo/cuentas
        sumTachoLargo = self.syncMotor_.leader.get_tacho().tacho_count + self.cuentasTamLargo_
        puedoAparcar = False

        while self.sensorUltraSound_.get_distance() > self.anchoCoche:
            
            if self.syncMotor_.leader.get_tacho().tacho_count > sumTachoLargo:
                puedoAparcar= True
                break

        print "Aparcarmiento: ", puedoAparcar

        self.syncMotor_.brake()
        time.sleep(1)

        if puedoAparcar:
            print "Tengo que ir hacia Atras"
            print "Marcha atras 1"
            self.syncMotor_.turn(-60, self.cuentasTamLargo_/2)
            time.sleep(1)
            self.syncMotor_.brake()
            print "Giro"
            self.syncMotor_.follower.weak_turn(60, self.cuentasGiro_/4)
            self.syncMotor_.leader.weak_turn(-60, self.cuentasGiro_/4)
            time.sleep(1.5)
            self.syncMotor_.brake()
            print "Marcha atras 2"
            self.syncMotor_.turn(-60, 3*(self.cuentasTamLargo_/4))
            time.sleep(1.5)
            self.syncMotor_.brake()
            self.syncMotor_.follower.weak_turn(-60, self.cuentasGiro_/4)
            self.syncMotor_.leader.weak_turn(60, self.cuentasGiro_/4)
            time.sleep(0.5)
            self.brick_.play_tone_and_wait(659, 500)
            #self.syncMotor_.turn(-70, self.cuentasTamLargo_/4)
        
        
        print "Fin"

if __name__=='__main__':
    # robot= Robot(nxt.locator.find_one_brick())
    robot= Robot(nxt.bluesock.BlueSock('00:16:53:09:46:3B').connect())
    robot.mision()
