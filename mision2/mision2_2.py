#!/usr/bin/env python

import nxt.bluesock
from nxt.sensor import *
import time


def connect(idmac):

    m = nxt.locator.Method(False, True, False, False)
    b = nxt.bluesock.BlueSock(idmac).connect()
    return b


def run(brick, line):

    # 1.Encedemos sensor de choque y esperemos el primer contacto
    sensor= Touch(brick, PORT_1)
    while sensor.get_sample()==0:
        pass;

    # 2.En los siguientes dos segundos esperamos contactos
    samples=1
    current_time= time.time()
    while (time.time() - current_time)<2.0:
        if(sensor.get_sample()==1):
            samples++


    print "samples",samples
    # 3.Encender Motor B y Motor C
    sync = SynchronizedMotors(Motor(brick, PORT_B),Motor(brick, PORT_C))
    
    # 1. Giro 45º y continuar recto
    # 2. Giro 90º sentido contrario y continuar
    # 3. Giro 180º y continuar
    # 4. Detener robot y mover brazo de arriba a abajo 2 veces


def __name__=='__main__':
    brick= connect('00:16:53:09:46:3B')
    line=0
    while (line<3):
        run(brick<line)
        line++

    # 4. Opcional. Emitir sonido como finalizacion
    brick.play_tone_and_wait(659, 500)