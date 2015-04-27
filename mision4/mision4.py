#robot intente localizar un objeto cercano con el sensor de ultrasonidos y se acerque a él, girando
#primero para apuntar al lugar en donde se encuentre el objeto y moviéndose luego
#hacia él hasta situarse a una distancia de unos 10 cm (esta distancia es aproximada y
#se debe validar experimentalmente). Al llegar a la distancia predeterminada, el robot
#debe mover el brazo y golpear el objeto.

#!/usr/bin/env python

import nxt.bluesock
import nxt.locator
from nxt.sensor import *
from nxt.motor import *
import time

class Robot:

    def __init__(self, brick):

        self.brick_= brick
        self.syncMotor_ = SynchronizedMotors(Motor(self.brick_, PORT_B), Motor(self.brick_, PORT_C), 0)
        self.arm_ = Motor(self.brick_, PORT_A)
        self.sensorUltraSound_= UltraSound(self.brick_, PORT_4)

        self.separationBetweenWheels_= 14
        self.cuenta_= ((encoder_*math.pi)/wheelDiameter_)
        turn_perimeter = (math.pi * self.wheelDiameter_) / 4
        self.cuentasGiro_ = turn_perimeter / self.cuenta_

    def mision(self):

        #1.Probar que mierdas devuelve cada funcion, falta probar los setters
        while True:
            print "Distance: ", self.sensorUltraSound_.get_distance()
            print "Measurament units: ", self.sensorUltraSound_.get_measurement_units()
            print "Interval: ", self.sensorUltraSound_.get_interval()
            print "All measuraments: ", self.sensorUltraSound_.get_all_measurements()


        # 3. Parar motores
        self.syncMotor_.idle()

        # 4. Opcional. Emitir sonido como finalizacion
        self.brick_.play_tone_and_wait(659, 500)


if __name__=='__main__':
    robot= Robot(nxt.locator.find_one_brick())
    #robot= Robot(nxt.bluesock.BlueSock('00:16:53:09:46:3B').connect())
    robot.mision()


