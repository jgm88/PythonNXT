#!/usr/bin/env python

import nxt.bluesock
from nxt.sensor import *
from nxt.motor import *
import time

class Robot:

    def __init__(self, brick):

        self.brick_= brick
        self.sensorTouch= Touch(self.brick_, PORT_1)
        self.syncMotor_ = SynchronizedMotors(Motor(self.brick_, PORT_B), Motor(self.brick_, PORT_C), 0)
        self.sensorLight_= Light(self.brick_, PORT_3)
        self.sensorLight_.set_illuminated(True)

    def mision(self):

        self.syncMotor_.run(80)
       
        # 1.Avanzar hasta encontrar linea negra
        while self.sensorLight_.get_lightness()<400:
           pass;
        
        self.syncMotor_.brake()

        # 2. Opcional. Emitir sonido como finalizacion
        self.brick_.play_tone_and_wait(659, 500)

if __name__=='__main__':
    robot= Robot(nxt.locator.find_one_brick())
    #robot= Robot(nxt.bluesock.BlueSock('00:16:53:09:46:3B').connect())
    robot.mision()