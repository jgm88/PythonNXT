#robot intente localizar un objeto cercano con el sensor de ultrasonidos y se acerque a él, girando
#primero para apuntar al lugar en donde se encuentre el objeto y moviéndose luego
#hacia él hasta situarse a una distancia de unos 10 cm (esta distancia es aproximada y
#se debe validar experimentalmente). Al llegar a la distancia predeterminada, el robot
#debe mover el brazo y golpear el objeto.

#!/usr/bin/env python

import nxt.bluesock
from nxt.sensor import *
from nxt.motor import *
import time
import msvcrt

def connect(idmac):

    b = nxt.bluesock.BlueSock(idmac).connect()
    return b


def run(brick):

    # 1.Encedemos sensor de luz
    sensor= UltraSound(brick, PORT_4)

    # 2.Encender Motor B y Motor C, sentido hacia adelante
    bPadre = Motor(brick, PORT_B)
    bHijo = Motor(brick, PORT_C)
    sync = SynchronizedMotors(bPadre, bHijo, 0) 
    sync.run(80)

    sync.brake()

    # 4. Opcional. Emitir sonido como finalizacion
    brick.play_tone_and_wait(659, 500)


if __name__=='__main__':
    brick= connect('00:16:53:09:46:3B')
    run(brick)