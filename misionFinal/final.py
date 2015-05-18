#!/usr/bin/env python

import nxt.bluesock
import nxt.locator
from nxt.sensor import *
from nxt.motor import *
import time
import math

class Robot:

    def __init__(self, brick, tam_encoder=360, wheel_diameter=5.6):

        self.brick_= brick
        self.syncMotor_ = SynchronizedMotors(Motor(self.brick_, PORT_B), Motor(self.brick_, PORT_C), 0)
        self.arm_ = Motor(self.brick_, PORT_A)
        self.sensorUltraSound_= Ultrasonic(self.brick_, PORT_1)

        self.separationBetweenWheels_= 14
        self.cuenta_= ((wheel_diameter*math.pi)/tam_encoder)
        turn_perimeter = (math.pi * 2.0 * self.separationBetweenWheels_) / 4.0
        self.cuentasGiro_ = turn_perimeter / self.cuenta_
        self.cuentasTam_ = 22.0 / self.cuenta_

    def mision(self):

        #1. Ir en linea recta hasta encontrar un objeto
        print "Buscanco Hueco"
        self.syncMotor_.run(70)
        anchoCoche = 25 #medida coche
        largoCoche = 22
        while self.sensorUltraSound_.get_distance() < anchoCoche: #medida del robot
            # print self.sensorUltraSound_.get_distance()
            pass
        print "Hueco Detectado"
        tachos = self.syncMotor_.leader.get_tacho().tacho_count
        puedoAparcar = False

        while self.sensorUltraSound_.get_distance() > largoCoche:

            if self.syncMotor_.leader.get_tacho().tacho_count > tachos + self.cuentasTam_:
                puedoAparcar= True
                break

        print "Aparcarmiento: ", puedoAparcar

        self.syncMotor_.brake()
        time.sleep(1)
        if puedoAparcar:
            print "Tengo k ir hacia Atras"
           
            #self.syncMotor_.turn(-70, self.cuentasTam_/4)
        print "Fin"

    def aparcar(self):
        self.syncMotor_.follower.weak_turn(60, self.cuentasGiro_/4)
        self.syncMotor_.leader.weak_turn(-60, self.cuentasGiro_/4)
        time.sleep(1.5)
        self.syncMotor_.brake()
        self.syncMotor_.turn(-60, 2*(self.cuentasTam_/3))
        time.sleep(1.5)
        self.syncMotor_.brake()
        self.syncMotor_.follower.weak_turn(-60, self.cuentasGiro_/4)
        self.syncMotor_.leader.weak_turn(60, self.cuentasGiro_/4)


if __name__=='__main__':
    robot= Robot(nxt.locator.find_one_brick())
    #robot= Robot(nxt.bluesock.BlueSock('00:16:53:09:46:3B').connect())
    #robot.mision()
    robot.aparcar()
