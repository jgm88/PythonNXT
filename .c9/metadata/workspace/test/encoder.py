{"filter":false,"title":"encoder.py","tooltip":"/test/encoder.py","undoManager":{"mark":43,"position":43,"stack":[[{"group":"doc","deltas":[{"start":{"row":0,"column":0},"end":{"row":21,"column":26},"action":"insert","lines":["#!/usr/bin/env python","","import nxt.locator","import nxt.bluesock","from nxt.motor import *","","def connect(idmac):","","    m = nxt.locator.Method(False, True, False, False)","    b = nxt.bluesock.BlueSock(idmac).connect()","    return b","","","if __name__=='__main__':","","    brick= connect('00:16:53:09:46:3B')","","    bPadre = Motor(brick, PORT_B)","    bHijo = Motor(brick, PORT_C)","    sync = SynchronizedMotors(bPadre, bHijo, 0)","","    print sync.get_tacho()"]}]}],[{"group":"doc","deltas":[{"start":{"row":20,"column":0},"end":{"row":21,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":3},"end":{"row":22,"column":26},"action":"remove","lines":[" print sync.get_tacho()"]},{"start":{"row":22,"column":3},"end":{"row":26,"column":16},"action":"insert","lines":["   current_time = time.time()","    sync.run(100)","    while (time.time() - current_time < 3.0):","        print \"Tacho: \", sync.get_tacho()","    sync.brake()"]}]}],[{"group":"doc","deltas":[{"start":{"row":4,"column":23},"end":{"row":5,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":5,"column":0},"end":{"row":5,"column":1},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":5,"column":1},"end":{"row":5,"column":2},"action":"insert","lines":["m"]}]}],[{"group":"doc","deltas":[{"start":{"row":5,"column":2},"end":{"row":5,"column":3},"action":"insert","lines":["p"]}]}],[{"group":"doc","deltas":[{"start":{"row":5,"column":3},"end":{"row":5,"column":4},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":5,"column":4},"end":{"row":5,"column":5},"action":"insert","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":5,"column":5},"end":{"row":5,"column":6},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":5,"column":7},"end":{"row":5,"column":8},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":5,"column":8},"end":{"row":5,"column":9},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":5,"column":9},"end":{"row":5,"column":10},"action":"insert","lines":["m"]}]}],[{"group":"doc","deltas":[{"start":{"row":5,"column":10},"end":{"row":5,"column":11},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":9,"column":1},"end":{"row":9,"column":53},"action":"remove","lines":["   m = nxt.locator.Method(False, True, False, False)"]}]}],[{"group":"doc","deltas":[{"start":{"row":9,"column":0},"end":{"row":9,"column":1},"action":"remove","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":0},"end":{"row":9,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":19},"end":{"row":8,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":17},"end":{"row":2,"column":18},"action":"remove","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":16},"end":{"row":2,"column":17},"action":"remove","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"remove","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":14},"end":{"row":2,"column":15},"action":"remove","lines":["a"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":13},"end":{"row":2,"column":14},"action":"remove","lines":["c"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":12},"end":{"row":2,"column":13},"action":"remove","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":11},"end":{"row":2,"column":12},"action":"remove","lines":["l"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"remove","lines":["."]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"remove","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"remove","lines":["x"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"remove","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"remove","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"remove","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":4},"end":{"row":2,"column":5},"action":"remove","lines":["r"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":3},"end":{"row":2,"column":4},"action":"remove","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":2},"end":{"row":2,"column":3},"action":"remove","lines":["p"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":1},"end":{"row":2,"column":2},"action":"remove","lines":["m"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"remove","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":20,"column":5},"end":{"row":20,"column":6},"action":"remove","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":20,"column":4},"end":{"row":20,"column":5},"action":"remove","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"remove","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":17,"column":47},"end":{"row":18,"column":0},"action":"remove","lines":["",""]}]}]]},"ace":{"folds":[],"scrolltop":18.5,"scrollleft":0,"selection":{"start":{"row":15,"column":33},"end":{"row":15,"column":33},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":9,"state":"start","mode":"ace/mode/python"}},"timestamp":1429604642182,"hash":"28c808d269cffc05630b9525147274b260236d0f"}