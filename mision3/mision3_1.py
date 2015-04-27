#!/usr/bin/env python

import nxt.bluesock
from nxt.sensor import *
from nxt.motor import *
import time
import msvcrt

#Programa en la que el robot avance
#indefinidamente hasta que alcance una linea negra. Si encuentra algun
#obstaculo, debe parar y cambiar de trayectoria.

def connect(idmac):

    m = nxt.locator.Method(False, True, False, False)
    b = nxt.bluesock.BlueSock(idmac).connect()
    return b


def run(brick):

    # 1.Encedemos sensor de luz
    sensor= Light(brick, PORT_3)
    sensor.set_illuminated(True)

    # 2.Encender Motor B y Motor C, sentido hacia adelante
    bPadre = Motor(brick, PORT_B)
    bHijo = Motor(brick, PORT_C)
    sync = SynchronizedMotors(bPadre, bHijo, 0) 
    sync.run(80)

    # 3.Avanzar hasta encontrar linea negra
    while sensor.get_lightness() < 500:
        pass;
        """
        print "Data:" , sensor.get_lightness()        
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if(key == "p"):
                print "PARO"
                break;     
                """
        
        #pass
    sync.brake()
    sensor.set_illuminated(False)

    # 4. Opcional. Emitir sonido como finalizacion
    brick.play_tone_and_wait(659, 500)


if __name__=='__main__':
    brick= connect('00:16:53:09:46:3B')
    run(brick)