#!/usr/bin/env python

import nxt.bluesock
from nxt.sensor import *
from nxt.motor import *
import time
import math

class Robot:

    def __init__(self, brick):

        self.brick_= brick
        self.separationBetweenWheels_= 8
        self.syncMotor_ = SynchronizedMotors(Motor(self.brick_, PORT_B), Motor(self.brick_, PORT_C), 0)
        self.cuenta_= ((encoder_*math.pi)/wheelDiameter_)
        self.sensorLight_= Light(brick, PORT_3)
        self.sensorLight_.set_illuminated(True)

        # 1. Calculamos las cuentas que tendra que pasar para girar hacia un stolado.
        # Si suponemos que un giro sobre si mismo es de de radio separationBewteenWheels, un giro solo ocupara una
        # cuarta parte del perimetro de la circunferencia.
        turn_perimeter = (math.pi * self.wheelDiameter_) / 4
        self.cuentasGiro_ = turn_perimeter / self.cuenta_

    def mision(self):

        num_line_max=0
        while (num_line_max<3):
          
            # 1.Mover hasta siguiente linea negra establecida por parametro
            self.syncMotor_.run(80)
            lines_passed=0
            while self.sensorLight_.get_lightness() < 400:
                if(line<lines_passed):
                    print "Paso linea: ", lines_passed
                    lines_passed++
            else:
              break
            self.syncMotor_.brake()

            # 2.Damos un giro de 180º y volvemos al inicio
            self.syncMotor_.leader.weak_turn(80, self.cuentasGiro_*2)
            self.syncMotor_.run(80, True)
            while self.sensorLight_.get_lightness() < 400:
                if(lines_passed>0):
                    print "Paso linea: ", lines_passed
                    lines_passed--
                else:
                    break
            self.syncMotor_.brake()
        
        num_line_max++
        
        # 3. Opcional. Emitir sonido como finalizacion
        self.brick_.play_tone_and_wait(659, 500)

if __name__=='__main__':
    #robot= Robot(nxt.locator.find_one_brick())
    robot= Robot(nxt.bluesock.BlueSock('00:16:53:09:46:3B').connect())
    robot.mision()
