#!/usr/bin/env python

import nxt.bluesock
from nxt.sensor import *
import time
from oct2py import octave


def connect(idmac):

    m = nxt.locator.Method(False, True, False, False)
    b = nxt.bluesock.BlueSock(idmac).connect()
    return b


def run(brick):

    # 1.Encedemos sensor de sonido
    sensor= Sound(b, PORT_2)

    # 2.Guardar todos los datos obtenidos en 10 segundos
    current_time= time.time()
    samples= []
    while (time.time() - current_time)<10.0:
        samples.append(sensor.get_sample())

    # 3.Usamos un script de octave para generar una grafica y decidir
    octave.plot(samples)

    # 4. Opcional. Emitir sonido como finalizacion
    brick.play_tone_and_wait(659, 500)

if __name__=='__main__':
    brick= connect('00:16:53:09:46:3B')
    run(brick)



