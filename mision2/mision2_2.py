#!/usr/bin/env python

import nxt.bluesock
from nxt.sensor import *
import time
from nxt.motor import *
import msvcrt


def connect(idmac):

    m = nxt.locator.Method(False, True, False, False)
    b = nxt.bluesock.BlueSock(idmac).connect()
    return b


def run(brick):

    # 1.Encedemos sensor de choque
    sensor = Touch(brick, PORT_1)
    
    # Encender Motor B y Motor C, sentido hacia adelante
    bPadre = Motor(brick, PORT_B)
    bHijo = Motor(brick, PORT_C)
    sync = SynchronizedMotors(bPadre, bHijo, 0)	
    
    print "Espero sensor de choque"
    while sensor.is_pressed() == False: 
        pass;    
    
    sync.run(70) # El sensor de choque lo tiene detras    

    # Esperamos a que vuelva a ser False
    while sensor.is_pressed() == True: 
        pass; 

    # 2.En los siguientes dos segundos esperamos contactos
    samples = 0
    current_time = time.time()

    print "Recolecto Samples"

    # Con estos semaforos nos aseguramos recolectar los samples correctos
    puedoRecolectar = False
    puedoSerPulsado = True

    while (time.time() - current_time)<2.0:                
        if(puedoSerPulsado and sensor.is_pressed()):
            puedoRecolectar = True
            puedoSerPulsado = False
        if(puedoRecolectar):
            puedoRecolectar = False
            samples+=1
        if(sensor.is_pressed() == False):
            puedoSerPulsado = True

    print "samples: ",samples
    
    sync.brake()

    # 1. Giro 45 y continuar recto
    if(samples == 1):
        bPadre.turn(100, 45)
        bHijo.turn(-100, 45)
        sync.run(70)
    # 2. Giro 90 sentido contrario y continuar
    elif(samples == 2):
        bPadre.turn(-100, 90)
        bHijo.turn(100, 90)
        sync.run(70)
    # 3. Giro 180 y continuar
    elif(samples == 3):
        bPadre.turn(100, 180)
        bHijo.turn(-100, 180)
        sync.run(70)
    # 4. Detener robot y mover brazo de arriba a abajo 2 veces
    elif(samples == 4):
        arm= Motor(brick, PORT_A)
        
        arm.reset_position(True)
        arm.turn(20, 50)
        arm.reset_position(True)        
        arm.turn(-20, 50)

        arm.reset_position(True)
        arm.turn(20, 50)
        arm.reset_position(True)        
        arm.turn(-20, 50)

    while True:            
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if(key == "p"):
                print "PARO"
                break;   
    sync.brake()

if __name__=='__main__':
    brick= connect('00:16:53:09:46:3B')
    run(brick)