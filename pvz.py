# -*- encoding=utf8 -*-
__author__ = "kangmeng"

from airtest.core.api import *

# auto_setup(__file__)

init_device(platform="IOS", uuid="http://192.168.124.16:8100")


from poco.drivers.ios import iosPoco
poco = iosPoco()

Pos1 = (911,665)
Pos2 = (1143,665)
Pos3 = (1357,665)
Pos4 = (917,917)
Pos5 = (1143,917)
Pos6 = (1357,917)
Pos7 = (911,1168)
Pos8 = (1143,1168)
Pos9 = (1357,1168)

freeze_poco = poco.freeze()
while(1):
    #开始战斗
    touch((2100,1558), duration=0.01)
    #等待开始
    sleep(6.2)

    #种花
    swipe((140,936),Pos4,duration=0.1,steps=0)
    swipe((157,1100),Pos7,duration=0.1,steps=0)
    #蓓蕾
    swipe((157,1418),Pos8,duration=0.1,steps=0)
    #收
    sleep(1)
    swipe((500,1000),(1500,1168),duration=0.1,steps=0)
    #swipe((450,1400),(1200,1400),duration=0.1,steps=0)

    #种花
    swipe((140,936),Pos1,duration=0.1,steps=0)
    swipe((157,1100),Pos8,duration=0.1,steps=0)

    #收
    #swipe((500,680),(1500,680),duration=0.1,steps=0)
    swipe((500,936),(1500,936),duration=0.1,steps=0)
    #swipe((500,1200),(1500,1200),duration=0.1,steps=0)


    #种花
    swipe((140,936),Pos2,duration=0.1,steps=0)
    swipe((157,1100),Pos9,duration=0.1,steps=0)

    #收
    #swipe((500,936),(1500,936),duration=0.1,steps=0)
    swipe((500,1200),(1500,1200),duration=0.1,steps=0)

    #种花
    swipe((140,936),Pos3,duration=0.1,steps=0)
    swipe((157,1100),Pos6,duration=0.1,steps=0)

    #种蛙
    swipe((150,1250),(1568,1123),duration=0.1,steps=0)
    
    #收能量豆
    swipe((1712,1100),(2200,1100),duration=1,steps=5)
    #swipe((1620,289),(1620,1400),duration=1,steps=5)


    #放能量豆
    sleep(0.3)
    swipe((527,1570),(1168,885),duration=0.1,steps=0)
    sleep(1.8)
    #收钱
    swipe((600,680),(1500,680),duration=0.1,steps=0)
    swipe((600,936),(1500,936),duration=0.1,steps=0)
    swipe((600,1150),(1500,1150),duration=0.1,steps=0)
    #重开
    touch((2298,96))
    sleep(0.5)
    touch((1203,1260))
    sleep(0.5)
    touch((1519,1160))
    sleep(8)# 
    

