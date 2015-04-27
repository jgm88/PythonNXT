#!/usr/bin/env python

import nxt.bluesock
from nxt.sensor import *
import time
import matplotlib.pyplot as plt

class Robot:

    def __init__(self, brick):

        self.brick_= brick
        self.sensorSound_= Sound(self.brick_, PORT_2)

    def mision(self):

        print "Get samples"
        current_time= time.time()
        samples= []
        aplausos=0
        puedoRecolectar = False
        puedoSerPulsado = True
        

        while (time.time() - current_time)<10.0:
            x= self.sensorSound_.get_sample()
            samples.append(x)
            
            if(puedoSerPulsado and x>600):
                puedoRecolectar = True
                puedoSerPulsado = False
            if(puedoRecolectar):
                puedoRecolectar = False
                aplausos+=1
            if(x < 600):
                puedoSerPulsado = True
           
            print "Sample: ", x

        print "Numero de aplausos: ", aplausos
        # 3.Usamos un script de octave para generar una grafica y decidir
        plt.plot(samples)
        plt.ylabel('Datos sonido')
        plt.show()

        # 4. Opcional. Emitir sonido como finalizacion
        self.brick_.play_tone_and_wait(659, 500)              
            

if __name__=='__main__':
    robot= Robot(nxt.locator.find_one_brick())
    #robot= Robot(nxt.bluesock.BlueSock('00:16:53:09:46:3B').connect())
    robot.mision()


