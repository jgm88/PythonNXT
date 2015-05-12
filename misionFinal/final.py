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
        self.cuentasTam_ = 30.0 / self.cuenta_

    def mision(self):

        #1. Ir en linea recta hasta encontrar un objeto
        print "Buscanco Hueco"
        self.syncMotor_.run(70)
        anchoCoche = 25 #medida coche
        largoCoche = 30
        while self.sensorUltraSound_.get_distance() < anchoCoche: #medida del robot
            # print self.sensorUltraSound_.get_distance()
            pass
        print "Hueco Detectado"
        tachos = self.syncMotor_.leader.get_tacho().tacho_count
        print "Tacho Inicial",tachos
        puedoImprimir = True
        print "cuenta", self.cuenta_
        print "CT", self.cuentasTam_
        while self.syncMotor_.leader.get_tacho().tacho_count < tachos + self.cuentasTam_:
            #  and self.sensorUltraSound_.get_distance() > anchoCoche
        # while self.sensorUltraSound_.get_distance() > anchoCoche: #medida del robot
            if puedoImprimir:
                print "Hueco Vacio"
                puedoImprimir = False
                pass
            pass
        print "Tacho Final",self.syncMotor_.leader.get_tacho().tacho_count

        self.syncMotor_.brake()
        time.sleep(1)

if __name__=='__main__':
    robot= Robot(nxt.locator.find_one_brick())
    #robot= Robot(nxt.bluesock.BlueSock('00:16:53:09:46:3B').connect())
    robot.mision()
