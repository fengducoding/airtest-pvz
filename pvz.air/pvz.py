# -*- encoding=utf8 -*-
__author__ = "kangmeng"

from airtest.core.api import *
#from airtest.core.settings import Setting as ST

ST.LOG_DIR = None
ST.LOG_FILE = None
ST.OPDELAY = 0.01

# auto_setup(__file__)

init_device(platform="IOS", uuid="http://192.168.124.13:8100")

#from poco.drivers.ios import iosPoco
#poco = iosPoco()

Pos1 = (911,665)
Pos2 = (1143,665)
Pos3 = (1357,665)
Pos4 = (917,917)
Pos5 = (1143,917)
Pos6 = (1357,917)
Pos7 = (911,1168)
Pos8 = (1143,1168)
Pos9 = (1357,1168)

fog1 = (1600,357)
fog2 = (1600,665)
fog3 = (1600,865)
fog4 = (1600,1102)
fog5 = (1600,1368)

engs1 = (1800,665)
engs2 = (1768,482)
engs3 = (1800,665)
engs4 = (1800,917)
engs5 = (1800,917)

engt1 = (911,665)
engt2 = (2180,732)
engt3 = (1357,665)
engt4 = (917,917)
engt5 = (1143,917)

fogpos = fog2
evgv1 = engs2
evgv2 = engt2

#freeze_poco = poco.freeze()
for i in range(1,51):
    touch(Template(r"tpl1643353238748.png", record_pos=(0.156, -0.119), resolution=(2388, 1668)))

    touch([665,778])
    touch([1231,1268])

    wait(Template(r"tpl1643353556755.png", record_pos=(-0.415, -0.321), resolution=(2388, 1668)))


    touch([2209,170])
    
    #
    touch([723,565])
    #tiaozhan
    touch([1189,1385])
    wait(Template(r"tpl1643352258647.png", record_pos=(-0.067, -0.082), resolution=(2388, 1668)))

    touch([2109,1501])
    wait(Template(r"tpl1643352386059.png", record_pos=(-0.359, -0.038), resolution=(2388, 1668)))

    #
    touch([723,565])
    touch(Template(r"tpl1643353638507.png", record_pos=(0.279, -0.167), resolution=(2388, 1668)))

    touch([728,594])
    text(str(i))

    touch([2284,1568])
    touch([1194,911])
    touch([653,1385])
    touch(Template(r"tpl1643353678235.png", record_pos=(-0.072, 0.149), resolution=(2388, 1668)))

    touch([1206,1206])
    touch([2009,224])
    touch([345,507])
    touch(Template(r"tpl1643353712807.png", record_pos=(0.338, -0.182), resolution=(2388, 1668)))

    touch([811,528])
    #zhantie
    touch([249,877])
    touch([1988,515])
    touch(Template(r"tpl1643349822742.png", record_pos=(-0.227, 0.004), resolution=(2388, 1668)))
    touch([1214,1393])
    wait(Template(r"tpl1643351633244.png", record_pos=(-0.067, 0.105), resolution=(2388, 1668)))

    touch([1011,1102])
    sleep(0.3)
    touch([2088,1501])


    wait(Template(r"tpl1643352386059.png", record_pos=(-0.359, -0.038), resolution=(2388, 1668)))
    touch([732,557])
    touch(Template(r"tpl1643349854278.png", record_pos=(-0.077, 0.02), resolution=(2388, 1668)))
    touch([1027,1189])
