#!/usr/bin/env python

import nxt.bluesock
from nxt.sensor import *
import time


def connect(idmac):

    m = nxt.locator.Method(False, True, False, False)
    b = nxt.bluesock.BlueSock(idmac).connect()
    return b


def run(brick):

    # 1.Encedemos sensor de luz
    sensor= Light(brick, PORT_3)

    # 2.Encender Motor B y Motor C, sentido hacia adelante
    sync = SynchronizedMotors(Motor(brick, PORT_B),Motor(brick, PORT_C))
    sync.run(100, True)

    # 3.Avanzar hasta encontrar linea negra
    while sensor.get_sample()>15:
        pass
    sync.brake()

    # 4. Opcional. Emitir sonido como finalizacion
    brick.play_tone_and_wait(659, 500)


if __name__=='__main__':
    brick= connect('00:16:53:09:46:3B')
    run(brick)