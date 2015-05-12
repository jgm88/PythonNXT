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
        self.sensorUltraSound_= Ultrasonic(self.brick_, PORT_4)

        self.separationBetweenWheels_= 14
        self.cuenta_= ((tam_encoder*math.pi)/wheel_diameter)
        turn_perimeter = (math.pi * 2.0 * self.separationBetweenWheels_) / 4.0
        self.cuentasGiro_ = turn_perimeter / self.cuenta_

    def mision(self):

        #1.Probar que mierdas devuelve cada funcion, falta probar los setters
        self.syncMotor_.leader.run(65)
        self.syncMotor_.follower.run(-65)
        minus= 255
        tm= time.time()

        #1. Vuelta para detectar el objeto mas cercano
        while time.time() - tm <=5.0:
            x= self.sensorUltraSound_.get_distance()
            if(x<minus):
                minus= x
        print "vuelta dada"
        print "Min distance: ", minus
        self.syncMotor_.brake()

        self.syncMotor_.leader.run(65)
        self.syncMotor_.follower.run(-65)

        #2. Vuelta y apuntar al objeto
        while self.sensorUltraSound_.get_distance() >= (minus+5):
            # print "estoy buscando"
            # print "sensor:", self.sensorUltraSound_.get_distance()
            pass;
        print "Stop"
        self.syncMotor_.brake()
        time.sleep(1)

        print "Arranco motores"
        self.syncMotor_.run(70)
        time.sleep(2)
        # self.syncMotor_.leader.run(65)
        # self.syncMotor_.follower.run(65)

        # self.syncMotor_.run(65)
        # distancia = self.sensorUltraSound_.get_distance()
        # print "Distancia: ", distancia
        while self.sensorUltraSound_.get_distance() <= 20: #Medida del brazo
            print "ir al objeto"
            pass;

        self.syncMotor_.brake()

        print "Toco objeto con el Brazo"
        self.arm_.turn(40,50)
        self.arm_.turn(-40,50)

        # 4. Opcional. Emitir sonido como finalizacion
        self.brick_.play_tone_and_wait(659, 500)
        print "FIN"


if __name__=='__main__':
    robot= Robot(nxt.locator.find_one_brick())
    #robot= Robot(nxt.bluesock.BlueSock('00:16:53:09:46:3B').connect())
    robot.mision()
