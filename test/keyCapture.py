#Solo testeado en windows

import msvcrt

#Equivalente a "cin>>"
opcion = raw_input("Seleccione la opcion: ")
print opcion

#Para escuchar
while True:
    if msvcrt.kbhit():
    	key = msvcrt.getch()
        print "Key pressed: " + key
        if(key == 'a'):
        	print "Pulsada a"
