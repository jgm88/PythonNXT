{"changed":false,"filter":false,"title":"mision1_1.py","tooltip":"/mision1/mision1_1.py","undoManager":{"mark":100,"position":100,"stack":[[{"group":"doc","deltas":[{"start":{"row":26,"column":18},"end":{"row":26,"column":19},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":26,"column":19},"end":{"row":26,"column":21},"action":"insert","lines":["()"]}]}],[{"group":"doc","deltas":[{"start":{"row":28,"column":38},"end":{"row":28,"column":39},"action":"remove","lines":["<"]}]}],[{"group":"doc","deltas":[{"start":{"row":28,"column":38},"end":{"row":28,"column":39},"action":"insert","lines":[">"]}]}],[{"group":"doc","deltas":[{"start":{"row":28,"column":39},"end":{"row":28,"column":40},"action":"insert","lines":["="]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":18},"end":{"row":29,"column":19},"action":"remove","lines":["'"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":17},"end":{"row":29,"column":18},"action":"remove","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":16},"end":{"row":29,"column":17},"action":"remove","lines":["u"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":15},"end":{"row":29,"column":16},"action":"remove","lines":["R"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":14},"end":{"row":29,"column":15},"action":"remove","lines":["'"]},{"start":{"row":29,"column":13},"end":{"row":29,"column":14},"action":"remove","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":12},"end":{"row":29,"column":13},"action":"remove","lines":["t"]},{"start":{"row":29,"column":11},"end":{"row":29,"column":12},"action":"remove","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":10},"end":{"row":29,"column":11},"action":"remove","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":9},"end":{"row":29,"column":10},"action":"remove","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":8},"end":{"row":29,"column":9},"action":"remove","lines":["p"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":8},"end":{"row":29,"column":9},"action":"insert","lines":["b"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":9},"end":{"row":29,"column":10},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":10},"end":{"row":29,"column":11},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":11},"end":{"row":29,"column":12},"action":"insert","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":12},"end":{"row":29,"column":13},"action":"insert","lines":["k"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":13},"end":{"row":29,"column":14},"action":"insert","lines":[";"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":8},"end":{"row":29,"column":14},"action":"remove","lines":["break;"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":0},"end":{"row":29,"column":8},"action":"remove","lines":["        "]}]}],[{"group":"doc","deltas":[{"start":{"row":28,"column":47},"end":{"row":29,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":28,"column":38},"end":{"row":28,"column":40},"action":"remove","lines":[">="]}]}],[{"group":"doc","deltas":[{"start":{"row":28,"column":38},"end":{"row":28,"column":39},"action":"insert","lines":[">"]}]}],[{"group":"doc","deltas":[{"start":{"row":28,"column":38},"end":{"row":28,"column":39},"action":"remove","lines":[">"]}]}],[{"group":"doc","deltas":[{"start":{"row":28,"column":38},"end":{"row":28,"column":39},"action":"insert","lines":[">"]}]}],[{"group":"doc","deltas":[{"start":{"row":28,"column":38},"end":{"row":28,"column":39},"action":"remove","lines":[">"]}]}],[{"group":"doc","deltas":[{"start":{"row":28,"column":38},"end":{"row":28,"column":39},"action":"insert","lines":[">"]}]}],[{"group":"doc","deltas":[{"start":{"row":28,"column":38},"end":{"row":28,"column":39},"action":"remove","lines":[">"]}]}],[{"group":"doc","deltas":[{"start":{"row":28,"column":38},"end":{"row":28,"column":39},"action":"insert","lines":["<"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":0},"end":{"row":26,"column":21},"action":"remove","lines":["    print current_time","    print time.time()"]}]}],[{"group":"doc","deltas":[{"start":{"row":24,"column":4},"end":{"row":25,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":24,"column":4},"end":{"row":25,"column":4},"action":"remove","lines":["","    "]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":0},"end":{"row":32,"column":12},"action":"remove","lines":["#!/usr/bin/env python","","import nxt.bluesock","from nxt.motor import *","import time","","#current_time = time.time()","#time.sleep(self._eta(tacho, tacho_target, power) / 2)","","def mision1_1(b):","    # Encender Motor B y Motor C, sentido hacia adelante","    m_left = Motor(b, PORT_B)","    m_right = Motor(b, PORT_C)","    ","    # Esperar 3 segundos","    time.sleep(3)","    ","    # Girar a la derecha","    m_right.turn(100, 90)","    ","    # Moverse hacia adelante durante 2 segundos","    current_time = time.time()","    m_left.run(100, True)","    m_right.run(100, True)","    ","    while (time.time() - current_time < 3.0) :","        ","    m_right.brake()","    m_left.brake()","","m = nxt.locator.Method(False, True, False, False)","b = nxt.bluesock.BlueSock('00:16:53:09:46:3B').connect()","mision1_1(b)"]},{"start":{"row":0,"column":0},"end":{"row":36,"column":12},"action":"insert","lines":["#!/usr/bin/env python","","import nxt.bluesock","from nxt.motor import *","import time","","#current_time = time.time()","#time.sleep(self._eta(tacho, tacho_target, power) / 2)","","def mision1_1(b):","    # Encender Motor B y Motor C, sentido hacia adelante","    m_left = Motor(b, PORT_B)","    m_right = Motor(b, PORT_C)","    ","    # Esperar 3 segundos","    time.sleep(3)","    ","    # Girar a la derecha","    m_right.turn(100, 90)","    time.sleep(1)","    # Moverse hacia adelante durante 2 segundos","    current_time = time.time()","    m_left.run(100, True)","    m_right.run(100, True)","    ","    print current_time","    print time.time()","    ","    while (time.time() - current_time < 3.0):","        pass        ","        ","    m_right.brake()","    m_left.brake()","","m = nxt.locator.Method(False, True, False, False)","b = nxt.bluesock.BlueSock('00:16:53:09:46:3B').connect()","mision1_1(b)"]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":0},"end":{"row":36,"column":12},"action":"remove","lines":["#!/usr/bin/env python","","import nxt.bluesock","from nxt.motor import *","import time","","#current_time = time.time()","#time.sleep(self._eta(tacho, tacho_target, power) / 2)","","def mision1_1(b):","    # Encender Motor B y Motor C, sentido hacia adelante","    m_left = Motor(b, PORT_B)","    m_right = Motor(b, PORT_C)","    ","    # Esperar 3 segundos","    time.sleep(3)","    ","    # Girar a la derecha","    m_right.turn(100, 90)","    time.sleep(1)","    # Moverse hacia adelante durante 2 segundos","    current_time = time.time()","    m_left.run(100, True)","    m_right.run(100, True)","    ","    print current_time","    print time.time()","    ","    while (time.time() - current_time < 3.0):","        pass        ","        ","    m_right.brake()","    m_left.brake()","","m = nxt.locator.Method(False, True, False, False)","b = nxt.bluesock.BlueSock('00:16:53:09:46:3B').connect()","mision1_1(b)"]},{"start":{"row":0,"column":0},"end":{"row":0,"column":21},"action":"insert","lines":["m_right.turn(100, 90)"]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":21},"end":{"row":37,"column":12},"action":"insert","lines":["#!/usr/bin/env python","","import nxt.bluesock","from nxt.motor import *","import time","","#current_time = time.time()","#time.sleep(self._eta(tacho, tacho_target, power) / 2)","","def mision1_1(b):","    # Encender Motor B y Motor C, sentido hacia adelante","    m_left = Motor(b, PORT_B)","    m_right = Motor(b, PORT_C)","    ","    # Esperar 3 segundos","    time.sleep(3)","    ","    # Girar a la derecha","    m_right.turn(100, 90)","    m_left.turn(-100, 90)","    time.sleep(1)","    # Moverse hacia adelante durante 2 segundos","    current_time = time.time()","    m_left.run(100, True)","    m_right.run(100, True)","    ","    print current_time","    print time.time()","    ","    while (time.time() - current_time < 3.0):","        pass        ","        ","    m_right.brake()","    m_left.brake()","","m = nxt.locator.Method(False, True, False, False)","b = nxt.bluesock.BlueSock('00:16:53:09:46:3B').connect()","mision1_1(b)"]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":0},"end":{"row":37,"column":12},"action":"remove","lines":["m_right.turn(100, 90)#!/usr/bin/env python","","import nxt.bluesock","from nxt.motor import *","import time","","#current_time = time.time()","#time.sleep(self._eta(tacho, tacho_target, power) / 2)","","def mision1_1(b):","    # Encender Motor B y Motor C, sentido hacia adelante","    m_left = Motor(b, PORT_B)","    m_right = Motor(b, PORT_C)","    ","    # Esperar 3 segundos","    time.sleep(3)","    ","    # Girar a la derecha","    m_right.turn(100, 90)","    m_left.turn(-100, 90)","    time.sleep(1)","    # Moverse hacia adelante durante 2 segundos","    current_time = time.time()","    m_left.run(100, True)","    m_right.run(100, True)","    ","    print current_time","    print time.time()","    ","    while (time.time() - current_time < 3.0):","        pass        ","        ","    m_right.brake()","    m_left.brake()","","m = nxt.locator.Method(False, True, False, False)","b = nxt.bluesock.BlueSock('00:16:53:09:46:3B').connect()","mision1_1(b)"]},{"start":{"row":0,"column":0},"end":{"row":37,"column":12},"action":"insert","lines":["#!/usr/bin/env python","","import nxt.bluesock","from nxt.motor import *","import time","","#current_time = time.time()","#time.sleep(self._eta(tacho, tacho_target, power) / 2)","","def mision1_1(b):","    # Encender Motor B y Motor C, sentido hacia adelante","    m_left = Motor(b, PORT_B)","    m_right = Motor(b, PORT_C)","    ","    # Esperar 3 segundos","    time.sleep(3)","    ","    # Girar a la derecha","    m_right.turn(100, 90)","    m_left.turn(-100, 90)","    time.sleep(1)","    # Moverse hacia adelante durante 2 segundos","    current_time = time.time()","    m_left.run(100, True)","    m_right.run(100, True)","    ","    print current_time","    print time.time()","    ","    while (time.time() - current_time < 3.0):","        pass        ","        ","    m_right.brake()","    m_left.brake()","","m = nxt.locator.Method(False, True, False, False)","b = nxt.bluesock.BlueSock('00:16:53:09:46:3B').connect()","mision1_1(b)"]}]}],[{"group":"doc","deltas":[{"start":{"row":37,"column":12},"end":{"row":38,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":38,"column":0},"end":{"row":39,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":0},"end":{"row":27,"column":21},"action":"remove","lines":["    ","    print current_time","    print time.time()"]}]}],[{"group":"doc","deltas":[{"start":{"row":20,"column":17},"end":{"row":21,"column":4},"action":"insert","lines":["","    "]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":0},"end":{"row":38,"column":0},"action":"remove","lines":["#!/usr/bin/env python","","import nxt.bluesock","from nxt.motor import *","import time","","#current_time = time.time()","#time.sleep(self._eta(tacho, tacho_target, power) / 2)","","def mision1_1(b):","    # Encender Motor B y Motor C, sentido hacia adelante","    m_left = Motor(b, PORT_B)","    m_right = Motor(b, PORT_C)","    ","    # Esperar 3 segundos","    time.sleep(3)","    ","    # Girar a la derecha","    m_right.turn(100, 90)","    m_left.turn(-100, 90)","    time.sleep(1)","    ","    # Moverse hacia adelante durante 2 segundos","    current_time = time.time()","    m_left.run(100, True)","    m_right.run(100, True)","","    ","    while (time.time() - current_time < 3.0):","        pass        ","        ","    m_right.brake()","    m_left.brake()","","m = nxt.locator.Method(False, True, False, False)","b = nxt.bluesock.BlueSock('00:16:53:09:46:3B').connect()","mision1_1(b)","",""]},{"start":{"row":0,"column":0},"end":{"row":35,"column":12},"action":"insert","lines":["#!/usr/bin/env python","","import nxt.bluesock","from nxt.motor import *","import time","","def mision1_1(b):","    # Encender Motor B y Motor C, sentido hacia adelante","    m_left = Motor(b, PORT_B)","    m_right = Motor(b, PORT_C)","    ","    # Esperar 3 segundos","    time.sleep(3)","    ","    # Girar a la derecha","    m_right.turn(100, 180)","    m_left.turn(-100, 180)","    ","    time.sleep(1)","    # Moverse hacia adelante durante 2 segundos","    current_time = time.time()","    m_left.run(100, True)","    m_right.run(100, True)","    ","    print current_time","    print time.time()","    ","    while (time.time() - current_time < 3.0):","        pass        ","        ","    m_right.brake()","    m_left.brake()","","m = nxt.locator.Method(False, True, False, False)","b = nxt.bluesock.BlueSock('00:16:53:09:46:3B').connect()","mision1_1(b)"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":56},"end":{"row":8,"column":4},"action":"insert","lines":["","    "]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":4},"end":{"row":8,"column":7},"action":"insert","lines":["syn"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":7},"end":{"row":8,"column":10},"action":"insert","lines":["c ="]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":11},"end":{"row":8,"column":13},"action":"insert","lines":["Sy"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":14},"end":{"row":8,"column":16},"action":"insert","lines":["ch"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":18},"end":{"row":8,"column":20},"action":"insert","lines":["ni"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":20},"end":{"row":8,"column":23},"action":"insert","lines":["zed"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":23},"end":{"row":8,"column":27},"action":"insert","lines":["Moto"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":27},"end":{"row":8,"column":29},"action":"insert","lines":["rs"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":29},"end":{"row":8,"column":31},"action":"insert","lines":["()"]}]}],[{"group":"doc","deltas":[{"start":{"row":9,"column":4},"end":{"row":9,"column":29},"action":"remove","lines":["m_left = Motor(b, PORT_B)"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":30},"end":{"row":8,"column":55},"action":"insert","lines":["m_left = Motor(b, PORT_B)"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":56},"end":{"row":9,"column":4},"action":"remove","lines":["","    "]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":30},"end":{"row":8,"column":33},"action":"remove","lines":["m_l"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":30},"end":{"row":8,"column":34},"action":"remove","lines":["eft "]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":30},"end":{"row":8,"column":32},"action":"remove","lines":["= "]}]}],[{"group":"doc","deltas":[{"start":{"row":9,"column":14},"end":{"row":9,"column":30},"action":"remove","lines":["Motor(b, PORT_C)"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":46},"end":{"row":8,"column":63},"action":"insert","lines":[",Motor(b, PORT_C)"]}]}],[{"group":"doc","deltas":[{"start":{"row":9,"column":10},"end":{"row":9,"column":14},"action":"remove","lines":["t = "]}]}],[{"group":"doc","deltas":[{"start":{"row":9,"column":6},"end":{"row":9,"column":10},"action":"remove","lines":["righ"]}]}],[{"group":"doc","deltas":[{"start":{"row":9,"column":4},"end":{"row":9,"column":6},"action":"remove","lines":["m_"]}]}],[{"group":"doc","deltas":[{"start":{"row":15,"column":4},"end":{"row":15,"column":8},"action":"remove","lines":["m_ri"]}]}],[{"group":"doc","deltas":[{"start":{"row":15,"column":4},"end":{"row":15,"column":7},"action":"remove","lines":["ght"]}]}],[{"group":"doc","deltas":[{"start":{"row":15,"column":4},"end":{"row":15,"column":6},"action":"insert","lines":["sy"]}]}],[{"group":"doc","deltas":[{"start":{"row":15,"column":6},"end":{"row":15,"column":8},"action":"insert","lines":["nc"]}]}],[{"group":"doc","deltas":[{"start":{"row":16,"column":4},"end":{"row":16,"column":5},"action":"insert","lines":["/"]}]}],[{"group":"doc","deltas":[{"start":{"row":16,"column":5},"end":{"row":16,"column":6},"action":"insert","lines":["/"]}]}],[{"group":"doc","deltas":[{"start":{"row":16,"column":5},"end":{"row":16,"column":6},"action":"remove","lines":["/"]}]}],[{"group":"doc","deltas":[{"start":{"row":16,"column":4},"end":{"row":16,"column":5},"action":"remove","lines":["/"]}]}],[{"group":"doc","deltas":[{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"remove","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":16,"column":0},"end":{"row":16,"column":1},"action":"insert","lines":["#"]}]}],[{"group":"doc","deltas":[{"start":{"row":21,"column":4},"end":{"row":21,"column":8},"action":"remove","lines":["m_le"]}]}],[{"group":"doc","deltas":[{"start":{"row":21,"column":4},"end":{"row":21,"column":6},"action":"remove","lines":["ft"]}]}],[{"group":"doc","deltas":[{"start":{"row":21,"column":4},"end":{"row":21,"column":5},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":21,"column":5},"end":{"row":21,"column":7},"action":"insert","lines":["yn"]}]}],[{"group":"doc","deltas":[{"start":{"row":21,"column":7},"end":{"row":21,"column":8},"action":"insert","lines":["c"]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":4},"end":{"row":22,"column":5},"action":"insert","lines":["#"]}]}],[{"group":"doc","deltas":[{"start":{"row":30,"column":4},"end":{"row":30,"column":7},"action":"remove","lines":["m_r"]}]}],[{"group":"doc","deltas":[{"start":{"row":30,"column":4},"end":{"row":30,"column":7},"action":"remove","lines":["igh"]}]}],[{"group":"doc","deltas":[{"start":{"row":30,"column":4},"end":{"row":30,"column":5},"action":"remove","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":30,"column":4},"end":{"row":30,"column":7},"action":"insert","lines":["syn"]}]}],[{"group":"doc","deltas":[{"start":{"row":30,"column":7},"end":{"row":30,"column":8},"action":"insert","lines":["c"]}]}],[{"group":"doc","deltas":[{"start":{"row":31,"column":4},"end":{"row":31,"column":5},"action":"insert","lines":["#"]}]}],[{"group":"doc","deltas":[{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":0},"end":{"row":35,"column":12},"action":"remove","lines":["#!/usr/bin/env python","","import nxt.bluesock","from nxt.motor import *","import time","","def mision1_1(b):","    # Encender Motor B y Motor C, sentido hacia adelante","    sync = SynchronizedMotors(Motor(b, PORT_B),Motor(b, PORT_C))","    ","    ","    # Esperar 3 segundos","    time.sleep(3)","    ","    # Girar a la derecha","    sync.turn(100, 180)","    #m_left.turn(-100, 180)","    ","    time.sleep(1)","    # Moverse hacia adelante durante 2 segundos","    current_time = time.time()","    sync.run(100, True)","    #m_right.run(100, True)","    ","    print current_time","    print time.time()","    ","    while (time.time() - current_time < 3.0):","        pass        ","        ","    sync.brake()","    #m_left.brake()","","m = nxt.locator.Method(False, True, False, False)","b = nxt.bluesock.BlueSock('00:16:53:09:46:3B').connect()","mision1_1(b)"]},{"start":{"row":0,"column":0},"end":{"row":75,"column":0},"action":"insert","lines":["#!/usr/bin/env python","","import nxt.bluesock","from nxt.motor import *","import time","","","def connect(idmac):","","    m = nxt.locator.Method(False, True, False, False)","    b = nxt.bluesock.BlueSock(idmac).connect()","    return b","","","# Mision","def run(brick):","    ","    # 1.Encender Motor B y Motor C, sentido hacia adelante","    sync = SynchronizedMotors(Motor(brick, PORT_B),Motor(brick, PORT_C))","    ","    # 2.Esperar 3 segundos","    time.sleep(3)","","    # 3.Girar a la derecha","    sync.turn(100, 180)","    time.sleep(1)","","    # 4.Moverse hacia adelante durante 2 segundos","    current_time = time.time()","    sync.run(100, True)","    while (time.time() - current_time < 2.0):","        pass        ","    sync.brake()","    ","    # 5.Girar a la izquierda","    sync.turn(-100, 180)","    time.sleep(1)","","    # 6.Moverse hacia adelante durante 3 segundos","    current_time = time.time()","    sync.run(100, True)","    while (time.time() - current_time < 3.0):","        pass        ","    sync.brake()","","    # 7.Girar a la izquierda","    sync.turn(-100, 180)","    time.sleep(1)","","    # 8.Moverse hacia adelante durante 1 segundos","    current_time = time.time()","    sync.run(100, True)","    while (time.time() - current_time < 1.0):","        pass        ","    sync.brake()","","    # 9. Para Motores B y C","    sync.disable()","","    # 10. Opcional. Emitir sonido como finalizacion","    brick.play_tone_and_wait(659, 500)","","","# Mision alternativa. Final a inicio.","def optional(b):","","     # 1.Encender Motor B y Motor C, sentido hacia adelante","    sync = SynchronizedMotors(Motor(b, PORT_B),Motor(b, PORT_C))","","def __name__=='__main__':","    brick= connect('00:16:53:09:46:3B')","    run(brick)","    optional(brick)","","",""]}]}],[{"group":"doc","deltas":[{"start":{"row":69,"column":0},"end":{"row":69,"column":3},"action":"remove","lines":["def"]},{"start":{"row":69,"column":0},"end":{"row":69,"column":1},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":69,"column":1},"end":{"row":69,"column":2},"action":"insert","lines":["f"]}]}],[{"group":"doc","deltas":[{"start":{"row":72,"column":3},"end":{"row":72,"column":4},"action":"insert","lines":["#"]}]}],[{"group":"doc","deltas":[{"start":{"row":73,"column":0},"end":{"row":75,"column":0},"action":"remove","lines":["","",""]}]}],[{"group":"doc","deltas":[{"start":{"row":72,"column":20},"end":{"row":73,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":0},"end":{"row":72,"column":20},"action":"remove","lines":["#!/usr/bin/env python","","import nxt.bluesock","from nxt.motor import *","import time","","","def connect(idmac):","","    m = nxt.locator.Method(False, True, False, False)","    b = nxt.bluesock.BlueSock(idmac).connect()","    return b","","","# Mision","def run(brick):","    ","    # 1.Encender Motor B y Motor C, sentido hacia adelante","    sync = SynchronizedMotors(Motor(brick, PORT_B),Motor(brick, PORT_C))","    ","    # 2.Esperar 3 segundos","    time.sleep(3)","","    # 3.Girar a la derecha","    sync.turn(100, 180)","    time.sleep(1)","","    # 4.Moverse hacia adelante durante 2 segundos","    current_time = time.time()","    sync.run(100, True)","    while (time.time() - current_time < 2.0):","        pass        ","    sync.brake()","    ","    # 5.Girar a la izquierda","    sync.turn(-100, 180)","    time.sleep(1)","","    # 6.Moverse hacia adelante durante 3 segundos","    current_time = time.time()","    sync.run(100, True)","    while (time.time() - current_time < 3.0):","        pass        ","    sync.brake()","","    # 7.Girar a la izquierda","    sync.turn(-100, 180)","    time.sleep(1)","","    # 8.Moverse hacia adelante durante 1 segundos","    current_time = time.time()","    sync.run(100, True)","    while (time.time() - current_time < 1.0):","        pass        ","    sync.brake()","","    # 9. Para Motores B y C","    sync.disable()","","    # 10. Opcional. Emitir sonido como finalizacion","    brick.play_tone_and_wait(659, 500)","","","# Mision alternativa. Final a inicio.","def optional(b):","","     # 1.Encender Motor B y Motor C, sentido hacia adelante","    sync = SynchronizedMotors(Motor(b, PORT_B),Motor(b, PORT_C))","","if __name__=='__main__':","    brick= connect('00:16:53:09:46:3B')","    run(brick)","   # optional(brick)"]},{"start":{"row":0,"column":0},"end":{"row":75,"column":20},"action":"insert","lines":["#!/usr/bin/env python","","import nxt.bluesock","from nxt.motor import *","import time","","","def connect(idmac):","","    m = nxt.locator.Method(False, True, False, False)","    b = nxt.bluesock.BlueSock(idmac).connect()","    return b","","","# Mision","def run(brick):","    ","    # 1.Encender Motor B y Motor C, sentido hacia adelante","    bPadre = Motor(brick, PORT_B)","    bHijo = Motor(brick, PORT_C)","    sync = SynchronizedMotors(bPadre, bHijo, 0)","    ","    # 2.Esperar 3 segundos","    time.sleep(3)","","    # 3.Girar a la derecha","    sync.turn(100, 25)","    time.sleep(1)","","    # 4.Moverse hacia adelante durante 2 segundos","    current_time = time.time()","    sync.run(100)","    while (time.time() - current_time < 2.0):","        pass;      ","    sync.brake()","    ","    # 5.Girar a la izquierda","    sync.turn(-100, 25)","    time.sleep(1)","","    # 6.Moverse hacia adelante durante 3 segundos","    current_time = time.time()","    sync.run(100)","    while (time.time() - current_time < 3.0):","        pass;       ","    sync.brake()","","    # 7.Girar a la izquierda","    sync.turn(-100, 25)","    time.sleep(1)","","    # 8.Moverse hacia adelante durante 1 segundos","    current_time = time.time()","    sync.run(100)","    while (time.time() - current_time < 1.0):","        pass;        ","    sync.brake()","","    # 9. Para Motores B y C","    sync._disable()","","    # 10. Opcional. Emitir sonido como finalizacion","    brick.play_tone_and_wait(659, 500)","","","# Mision alternativa. Final a inicio.","def optional(b):","","    bPadre = Motor(brick, PORT_B)","    bHijo = Motor(brick, PORT_C)","    sync = SynchronizedMotors(bPadre, bHijo, 0)","","if __name__=='__main__':","    brick= connect('00:16:53:09:46:3B')","    run(brick)","    #optional(brick)"]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":0},"end":{"row":75,"column":20},"action":"remove","lines":["#!/usr/bin/env python","","import nxt.bluesock","from nxt.motor import *","import time","","","def connect(idmac):","","    m = nxt.locator.Method(False, True, False, False)","    b = nxt.bluesock.BlueSock(idmac).connect()","    return b","","","# Mision","def run(brick):","    ","    # 1.Encender Motor B y Motor C, sentido hacia adelante","    bPadre = Motor(brick, PORT_B)","    bHijo = Motor(brick, PORT_C)","    sync = SynchronizedMotors(bPadre, bHijo, 0)","    ","    # 2.Esperar 3 segundos","    time.sleep(3)","","    # 3.Girar a la derecha","    sync.turn(100, 25)","    time.sleep(1)","","    # 4.Moverse hacia adelante durante 2 segundos","    current_time = time.time()","    sync.run(100)","    while (time.time() - current_time < 2.0):","        pass;      ","    sync.brake()","    ","    # 5.Girar a la izquierda","    sync.turn(-100, 25)","    time.sleep(1)","","    # 6.Moverse hacia adelante durante 3 segundos","    current_time = time.time()","    sync.run(100)","    while (time.time() - current_time < 3.0):","        pass;       ","    sync.brake()","","    # 7.Girar a la izquierda","    sync.turn(-100, 25)","    time.sleep(1)","","    # 8.Moverse hacia adelante durante 1 segundos","    current_time = time.time()","    sync.run(100)","    while (time.time() - current_time < 1.0):","        pass;        ","    sync.brake()","","    # 9. Para Motores B y C","    sync._disable()","","    # 10. Opcional. Emitir sonido como finalizacion","    brick.play_tone_and_wait(659, 500)","","","# Mision alternativa. Final a inicio.","def optional(b):","","    bPadre = Motor(brick, PORT_B)","    bHijo = Motor(brick, PORT_C)","    sync = SynchronizedMotors(bPadre, bHijo, 0)","","if __name__=='__main__':","    brick= connect('00:16:53:09:46:3B')","    run(brick)","    #optional(brick)"]},{"start":{"row":0,"column":0},"end":{"row":84,"column":0},"action":"insert","lines":["#!/usr/bin/env python","","import nxt.bluesock","from nxt.motor import *","import time","","","def connect(idmac):","","    m = nxt.locator.Method(False, True, False, False)","    b = nxt.bluesock.BlueSock(idmac).connect()","    return b","","","# Mision","def run(brick):","    ","    # 1.Encender Motor B y Motor C, sentido hacia adelante","    bPadre = Motor(brick, PORT_B)","    bHijo = Motor(brick, PORT_C)","    sync = SynchronizedMotors(bPadre, bHijo, 0)","    ","    # 2.Moverse hacia adelante durante 3 segundos","    current_time = time.time()","    sync.run(100)","    while (time.time() - current_time < 3.0):","        pass;      ","    sync.brake()","","    # 3.Girar a la derecha","    bPadre.turn(100, 180)","    bHijo.turn(-100, 180)","    time.sleep(1)","","    # 4.Moverse hacia adelante durante 2 segundos","    current_time = time.time()","    sync.run(100)","    while (time.time() - current_time < 2.0):","        pass;      ","    sync.brake()","    ","    # 5.Girar a la izquierda","    bPadre.turn(-100, 180)","    bHijo.turn(100, 180)","    time.sleep(1)","","    # 6.Moverse hacia adelante durante 3 segundos","    current_time = time.time()","    sync.run(100)","    while (time.time() - current_time < 3.0):","        pass;       ","    sync.brake()","","    # 7.Girar a la izquierda","    bPadre.turn(-100, 180)","    bHijo.turn(100, 180)","    time.sleep(1)","","    # 8.Moverse hacia adelante durante 1 segundos","    current_time = time.time()","    sync.run(100)","    while (time.time() - current_time < 1.0):","        pass;        ","    sync.brake()","","    # 9. Para Motores B y C","    sync._disable()","","    # 10. Opcional. Emitir sonido como finalizacion","    brick.play_tone_and_wait(659, 500)","","","# Mision alternativa. Final a inicio.","def optional(b):","","    m_left = Motor(b, PORT_B)","    m_left.turn(100, 180)","    m_right = Motor(b, PORT_C)","    m_right.turn(-100, 180)","","if __name__=='__main__':","    brick= connect('00:16:53:09:46:3B')","    run(brick)","    #optional(brick)",""]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":0},"end":{"row":84,"column":0},"action":"remove","lines":["#!/usr/bin/env python","","import nxt.bluesock","from nxt.motor import *","import time","","","def connect(idmac):","","    m = nxt.locator.Method(False, True, False, False)","    b = nxt.bluesock.BlueSock(idmac).connect()","    return b","","","# Mision","def run(brick):","    ","    # 1.Encender Motor B y Motor C, sentido hacia adelante","    bPadre = Motor(brick, PORT_B)","    bHijo = Motor(brick, PORT_C)","    sync = SynchronizedMotors(bPadre, bHijo, 0)","    ","    # 2.Moverse hacia adelante durante 3 segundos","    current_time = time.time()","    sync.run(100)","    while (time.time() - current_time < 3.0):","        pass;      ","    sync.brake()","","    # 3.Girar a la derecha","    bPadre.turn(100, 180)","    bHijo.turn(-100, 180)","    time.sleep(1)","","    # 4.Moverse hacia adelante durante 2 segundos","    current_time = time.time()","    sync.run(100)","    while (time.time() - current_time < 2.0):","        pass;      ","    sync.brake()","    ","    # 5.Girar a la izquierda","    bPadre.turn(-100, 180)","    bHijo.turn(100, 180)","    time.sleep(1)","","    # 6.Moverse hacia adelante durante 3 segundos","    current_time = time.time()","    sync.run(100)","    while (time.time() - current_time < 3.0):","        pass;       ","    sync.brake()","","    # 7.Girar a la izquierda","    bPadre.turn(-100, 180)","    bHijo.turn(100, 180)","    time.sleep(1)","","    # 8.Moverse hacia adelante durante 1 segundos","    current_time = time.time()","    sync.run(100)","    while (time.time() - current_time < 1.0):","        pass;        ","    sync.brake()","","    # 9. Para Motores B y C","    sync._disable()","","    # 10. Opcional. Emitir sonido como finalizacion","    brick.play_tone_and_wait(659, 500)","","","# Mision alternativa. Final a inicio.","def optional(b):","","    m_left = Motor(b, PORT_B)","    m_left.turn(100, 180)","    m_right = Motor(b, PORT_C)","    m_right.turn(-100, 180)","","if __name__=='__main__':","    brick= connect('00:16:53:09:46:3B')","    run(brick)","    #optional(brick)",""]},{"start":{"row":0,"column":0},"end":{"row":84,"column":0},"action":"insert","lines":["#!/usr/bin/env python","","import nxt.bluesock","from nxt.motor import *","import time","","","def connect(idmac):","","    m = nxt.locator.Method(False, True, False, False)","    b = nxt.bluesock.BlueSock(idmac).connect()","    return b","","","# Mision","def run(brick):","    ","    # 1.Encender Motor B y Motor C, sentido hacia adelante","    bPadre = Motor(brick, PORT_B)","    bHijo = Motor(brick, PORT_C)","    sync = SynchronizedMotors(bPadre, bHijo, 0)","    ","    # 2.Moverse hacia adelante durante 3 segundos","    current_time = time.time()","    sync.run(100)","    while (time.time() - current_time < 3.0):","        pass;      ","    sync.brake()","","    # 3.Girar a la derecha","    bPadre.turn(100, 180)","    bHijo.turn(-100, 180)","    time.sleep(1)","","    # 4.Moverse hacia adelante durante 2 segundos","    current_time = time.time()","    sync.run(100)","    while (time.time() - current_time < 2.0):","        pass;      ","    sync.brake()","    ","    # 5.Girar a la izquierda","    bPadre.turn(-100, 180)","    bHijo.turn(100, 180)","    time.sleep(1)","","    # 6.Moverse hacia adelante durante 3 segundos","    current_time = time.time()","    sync.run(100)","    while (time.time() - current_time < 3.0):","        pass;       ","    sync.brake()","","    # 7.Girar a la izquierda","    bPadre.turn(-100, 180)","    bHijo.turn(100, 180)","    time.sleep(1)","","    # 8.Moverse hacia adelante durante 1 segundos","    current_time = time.time()","    sync.run(100)","    while (time.time() - current_time < 1.0):","        pass;        ","    sync.brake()","","    # 9. Para Motores B y C","    sync._disable()","","    # 10. Opcional. Emitir sonido como finalizacion","    brick.play_tone_and_wait(659, 500)","","","# Mision alternativa. Final a inicio.","def optional(b):","","    m_left = Motor(b, PORT_B)","    m_left.turn(100, 180)","    m_right = Motor(b, PORT_C)","    m_right.turn(-100, 180)","","if __name__=='__main__':","    brick= connect('00:16:53:09:46:3B')","    run(brick)","    #optional(brick)",""]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":0},"end":{"row":84,"column":0},"action":"remove","lines":["#!/usr/bin/env python","","import nxt.bluesock","from nxt.motor import *","import time","","","def connect(idmac):","","    m = nxt.locator.Method(False, True, False, False)","    b = nxt.bluesock.BlueSock(idmac).connect()","    return b","","","# Mision","def run(brick):","    ","    # 1.Encender Motor B y Motor C, sentido hacia adelante","    bPadre = Motor(brick, PORT_B)","    bHijo = Motor(brick, PORT_C)","    sync = SynchronizedMotors(bPadre, bHijo, 0)","    ","    # 2.Moverse hacia adelante durante 3 segundos","    current_time = time.time()","    sync.run(100)","    while (time.time() - current_time < 3.0):","        pass;      ","    sync.brake()","","    # 3.Girar a la derecha","    bPadre.turn(100, 180)","    bHijo.turn(-100, 180)","    time.sleep(1)","","    # 4.Moverse hacia adelante durante 2 segundos","    current_time = time.time()","    sync.run(100)","    while (time.time() - current_time < 2.0):","        pass;      ","    sync.brake()","    ","    # 5.Girar a la izquierda","    bPadre.turn(-100, 180)","    bHijo.turn(100, 180)","    time.sleep(1)","","    # 6.Moverse hacia adelante durante 3 segundos","    current_time = time.time()","    sync.run(100)","    while (time.time() - current_time < 3.0):","        pass;       ","    sync.brake()","","    # 7.Girar a la izquierda","    bPadre.turn(-100, 180)","    bHijo.turn(100, 180)","    time.sleep(1)","","    # 8.Moverse hacia adelante durante 1 segundos","    current_time = time.time()","    sync.run(100)","    while (time.time() - current_time < 1.0):","        pass;        ","    sync.brake()","","    # 9. Para Motores B y C","    sync._disable()","","    # 10. Opcional. Emitir sonido como finalizacion","    brick.play_tone_and_wait(659, 500)","","","# Mision alternativa. Final a inicio.","def optional(b):","","    m_left = Motor(b, PORT_B)","    m_left.turn(100, 180)","    m_right = Motor(b, PORT_C)","    m_right.turn(-100, 180)","","if __name__=='__main__':","    brick= connect('00:16:53:09:46:3B')","    run(brick)","    #optional(brick)",""]},{"start":{"row":0,"column":0},"end":{"row":86,"column":0},"action":"insert","lines":["#!/usr/bin/env python","","import nxt.bluesock","from nxt.motor import *","import time","","","def connect(idmac):","","    m = nxt.locator.Method(False, True, False, False)","    b = nxt.bluesock.BlueSock(idmac).connect()","    return b","","","# Mision","def run(brick):","    ","    # 1.Encender Motor B y Motor C, sentido hacia adelante","    bPadre = Motor(brick, PORT_B)","    bHijo = Motor(brick, PORT_C)","    sync = SynchronizedMotors(bPadre, bHijo, 0)","    ","    # 2.Moverse hacia adelante durante 3 segundos","    current_time = time.time()","    sync.run(100)","    while (time.time() - current_time < 3.0):","        pass;      ","    sync.brake()","","    ## EL GIRO DEBERIA SER IGUAL, COMPENSAMOS LOS MOTORES","","    # 3.Girar a la derecha","    bPadre.turn(100, 180)","    bHijo.turn(-100, 180)","    time.sleep(1)","","    # 4.Moverse hacia adelante durante 2 segundos","    current_time = time.time()","    sync.run(100)","    while (time.time() - current_time < 2.0):","        pass;      ","    sync.brake()","    ","    # 5.Girar a la izquierda","    bPadre.turn(-100, 180)","    bHijo.turn(100, 180)","    time.sleep(1)","","    # 6.Moverse hacia adelante durante 3 segundos","    current_time = time.time()","    sync.run(100)","    while (time.time() - current_time < 3.0):","        pass;       ","    sync.brake()","","    # 7.Girar a la izquierda","    bPadre.turn(-100, 180)","    bHijo.turn(100, 180)","    time.sleep(1)","","    # 8.Moverse hacia adelante durante 1 segundos","    current_time = time.time()","    sync.run(100)","    while (time.time() - current_time < 1.0):","        pass;        ","    sync.brake()","","    # 9. Para Motores B y C","    sync._disable()","","    # 10. Opcional. Emitir sonido como finalizacion","    brick.play_tone_and_wait(659, 500)","","","# Mision alternativa. Final a inicio.","def optional(b):","","    m_left = Motor(b, PORT_B)","    m_left.turn(100, 180)","    m_right = Motor(b, PORT_C)","    m_right.turn(-100, 180)","","if __name__=='__main__':","    brick= connect('00:16:53:09:46:3B')","    run(brick)","    #optional(brick)",""]}]}]]},"ace":{"folds":[],"scrolltop":240,"scrollleft":0,"selection":{"start":{"row":23,"column":30},"end":{"row":23,"column":30},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":15,"state":"start","mode":"ace/mode/python"}},"timestamp":1429004844000}