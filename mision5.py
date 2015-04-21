#!/usr/bin/env python

import nxt.bluesock
from nxt.sensor import *
import time
#from oct2py import octave
import matplotlib.pyplot as plt

# que cuente el numero de veces que aplaudimos
# en un periodo de 10 segundos. El resultado debe mostrarse en la pantalla del PC, asi
# como una grafica en la que se dibuje la intensidad del sonido que se ha ido obteniendo
# en esos 10 segundos.

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
    #octave.plot(samples)
    
    plt.plot(samples)
    plt.ylabel('Datos sonido')
    plt.show()

    # 4. Opcional. Emitir sonido como finalizacion
    brick.play_tone_and_wait(659, 500)

if __name__=='__main__':
    brick= connect('00:16:53:09:46:3B')
    run(brick)


