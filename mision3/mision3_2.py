#!/usr/bin/env python

import nxt.bluesock
from nxt.sensor import *
import time


def connect(idmac):

    m = nxt.locator.Method(False, True, False, False)
    b = nxt.bluesock.BlueSock(idmac).connect()
    return b


def run(brick, line):

    # 1.Encedemos sensor de luz
    sensor= Light(brick, PORT_3)
    sensor.set_illuminated(True)

    # 2.Encender Motor B y Motor C, sentido hacia adelante
    sync = SynchronizedMotors(Motor(brick, PORT_B),Motor(brick, PORT_C))
    sync.run(80, True)

    # 3.Mover hasta la linea line
    lines_passed=0
    while sensor.get_lightness() < 500:
        if(line<lines_passed):
            lines_passed++
        else:
            break
    sync.brake()

    #3.Volvemos al inicio ¡¡¡¡¡marcha atras!!!!, en el pdf pone giro sobre si mismo, hay que preguntar si esto se puede tambien, sino cambiaremos por giro
    sync.run(-80, True)
    while sensor.get_sample()>15:
        if(lines_passed!=0):
            lines_passed++
        else:
            break
    sync.brake()


def __name__=='__main__':
    brick= connect('00:16:53:09:46:3B')
    line=0
    while (line<3):
        run(brick<line)
        line++

    # 4. Opcional. Emitir sonido como finalizacion
    brick.play_tone_and_wait(659, 500)