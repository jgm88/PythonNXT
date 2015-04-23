#!/usr/bin/env python

import nxt.bluesock
from nxt.motor import *
import math
import time

class Robot:

    def __init__(self, brick, tam_encoder=360, wheel_diameter=5.6):
        
        self.brick_= brick
        self.separationBetweenWheels_= 8
        self.syncMotor_ = SynchronizedMotors(Motor(self.brick_, PORT_B), Motor(self.brick_, PORT_C), 0)
        self.cuenta_= ((encoder_*math.pi)/wheelDiameter_)

        # 1. Calculamos las cuentas que tendra que pasar para girar hacia un stolado.
        # Si suponemos que un giro sobre si mismo es de de radio separationBewteenWheels, un giro solo ocupara una
        # cuarta parte del perimetro de la circunferencia.
        turn_perimeter = (math.pi * self.wheelDiameter_) / 4
        self.cuentasGiro = turn_perimeter / self.cuenta_

    def moveTurnTime(self,time):
         current_time = time.time()
        self.syncMotor_.run(80)
        while (time.time() - current_time < time):
            pass;      
        sync.brake()

    def mision(self):

        # 1.Mover robot hacia delante 3 segundos
        moveTurnTime(3.0)

        # 2.Girar a la derecha
        self.syncMotor_.follower.weak_turn(80, self.cuentasGiro)


        # 3.Mover robot hacia delante 2 segundos
        moveTurnTime(2.0)

        # 4. Girar a la izquierda
        self.syncMotor_.leader.weak_turn(80, self.cuentasGiro)

        # 5. Moverse hacia delante 1 segundos
        moveTurnTime(1.0)

        # 6. Dessincrnizacion motores
        self.syncMotor_.idle()

        # 7. Emitir sonido de finalizacion
        self.brick_.play_tone_and_wait(659, 500)

if __name__=='__main__':
    #robot= Robot(nxt.locator.find_one_brick())
    robot= Robot(nxt.bluesock.BlueSock('00:16:53:09:46:3B').connect())
    robot.mision()