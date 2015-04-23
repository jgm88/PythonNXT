#!/usr/bin/env python

import nxt.bluesock
from nxt.motor import *
from nxt.sensor import *
import time

class Robot:

    def __init__(self, brick):

        self.brick_= brick
        self.sensorTouch= Touch(self.brick, PORT_1)
        self.syncMotor_ = SynchronizedMotors(Motor(self.brick_, PORT_B), Motor(self.brick_, PORT_C), 0)


    def mision(self):

        # 1.Mover hacia delante hasta que se pulse el sensor de choque
        self.syncMotor_.run(-100)
        
        while self.sensorTouch.is_pressed()==False: 
            pass;    

        self.syncMotor_.brake()
        self.syncMotor_.idle()   

        # 2. Opcional. Emitir sonido como finalizacion
        self.brick_brick.play_tone_and_wait(659, 500)                              

        self.brick_.play_tone_and_wait(659, 500)

if __name__=='__main__':
    #robot= Robot(nxt.locator.find_one_brick())
    robot= Robot(nxt.bluesock.BlueSock('00:16:53:09:46:3B').connect())
    robot.mision()