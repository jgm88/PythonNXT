#!/usr/bin/env python

import nxt.bluesock
from nxt.motor import *
from nxt.sensor import *
import time

#Realiza un programa en el que el robot se
#mueva indefinidamente hacia adelante hasta que detecte un choque.

def connect(idmac):

    m = nxt.locator.Method(False, True, False, False)
    b = nxt.bluesock.BlueSock(idmac).connect()
    return b


def run(brick):

    # 1.Encedemos sensor de choque
    sensor = Touch(brick, PORT_1)

    # 2.Encender Motor B y Motor C, sentido hacia adelante
    bPadre = Motor(brick, PORT_B)
    bHijo = Motor(brick, PORT_C)
    sync = SynchronizedMotors(bPadre, bHijo, 0)	
    sync.run(-100) # El sensor de choque lo tiene detras

    while sensor.is_pressed()==False: 
        pass;    

    sync.brake()                  


if __name__=='__main__':
    brick= connect('00:16:53:09:46:3B')
    run(brick)