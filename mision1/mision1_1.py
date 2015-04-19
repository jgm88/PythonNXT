#!/usr/bin/env python

import nxt.bluesock
from nxt.motor import *
import time


def connect(idmac):

    m = nxt.locator.Method(False, True, False, False)
    b = nxt.bluesock.BlueSock(idmac).connect()
    return b


# Mision
def run(brick):
    
    # 1.Encender Motor B y Motor C, sentido hacia adelante
    bPadre = Motor(brick, PORT_B)
    bHijo = Motor(brick, PORT_C)
    sync = SynchronizedMotors(bPadre, bHijo, 0)
    
    # 2.Moverse hacia adelante durante 3 segundos
    current_time = time.time()
    sync.run(100)
    while (time.time() - current_time < 3.0):
        pass;      
    sync.brake()

    ## EL GIRO DEBERIA SER IGUAL, COMPENSAMOS LOS MOTORES

    # 3.Girar a la derecha
    bPadre.turn(100, 180)
    bHijo.turn(-100, 180)
    time.sleep(1)

    # 4.Moverse hacia adelante durante 2 segundos
    current_time = time.time()
    sync.run(100)
    while (time.time() - current_time < 2.0):
        pass;      
    sync.brake()
    
    # 5.Girar a la izquierda
    bPadre.turn(-100, 180)
    bHijo.turn(100, 180)
    time.sleep(1)

    # 6.Moverse hacia adelante durante 3 segundos
    current_time = time.time()
    sync.run(100)
    while (time.time() - current_time < 3.0):
        pass;       
    sync.brake()

    # 7.Girar a la izquierda
    bPadre.turn(-100, 180)
    bHijo.turn(100, 180)
    time.sleep(1)

    # 8.Moverse hacia adelante durante 1 segundos
    current_time = time.time()
    sync.run(100)
    while (time.time() - current_time < 1.0):
        pass;        
    sync.brake()

    # 9. Para Motores B y C
    sync._disable()

    # 10. Opcional. Emitir sonido como finalizacion
    brick.play_tone_and_wait(659, 500)


# Mision alternativa. Final a inicio.
def optional(b):

    m_left = Motor(b, PORT_B)
    m_left.turn(100, 180)
    m_right = Motor(b, PORT_C)
    m_right.turn(-100, 180)

if __name__=='__main__':
    brick= connect('00:16:53:09:46:3B')
    run(brick)
    #optional(brick)
