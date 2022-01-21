# -*- encoding=utf8 -*-
__author__ = "kangmeng"

import wda
import time

# Settings
wda.DEBUG = False
wda.HTTP_TIMEOUT = 20.0

# Enable debug will see http Request and Response
# wda.DEBUG = True
#c = wda.USBClient()
c = wda.Client('http://10.4.104.13:8100')

# Show status
#print c.status()

# Wait WDA ready
#c.wait_ready(timeout=300) # 等待300s,默认120s
c.wait_ready(timeout=300, noprint=True) # 安静的等待,无进度输出

#print(c.appium_settings())
'''
{
    'boundElementsByIndex': False, 
    'mjpegServerFramerate': 10, 
    'screenshotOrientation': 'auto', 
    'reduceMotion': False, 
    'elementResponseAttributes': 'type,label', 
    'screenshotQuality': 1, 
    'mjpegScalingFactor': 100, 
    'keyboardPrediction': 0, 
    'defaultActiveApplication': 'auto', 
    'mjpegServerScreenshotQuality': 25, 
    'defaultAlertAction': '', 
    'keyboardAutocorrection': 0, 
    'useFirstMatch': False, 
    'shouldUseCompactResponses': True, 
    'customSnapshotTimeout': 15, 
    'dismissAlertButtonSelector': '', 
    'activeAppDetectionPoint': '153.60,153.60', 
    'snapshotMaxDepth': 50, 
    'waitForIdleTimeout': 10, 
    'includeNonModalElements': False, 
    'acceptAlertButtonSelector': '', 
    'animationCoolOffTimeout': 2
}
'''
#c.home()

#s = c.session()
#print(s.orientation)
#s.close()
#print(s.window_size())
#print(c.source())
#c.click(0.88,0.93)
#c.screenshot().save("2.png")


#预定义位置  #2388  1668   * 0.5
cardx = 70
cardy1 = 138
cardy2 = 222
cardy3 = 300
cardy4 = 380
cardy5 = 460
cardy6 = 540
cardy7 = 622
cardy8 = 705

x1 = 240
x2 = 345
x3 = 450    
x4 = 560
x5 = 670
x6 = 780
x7 = 886
x8 = 988
x9 = 1098

y1 = 176
y2 = 303
y3 = 428
y4 = 556
y5 = 677

#收能量花路径
et1 = [888, 140]
et2 = [933, 250]
et3 = [933, 360]
et4 = [933, 470]
et5 = [971, 611]

pos1 = [x3,y2]
pos2 = [x4,y2]
pos3 = [x5,y2]
pos4 = [x3,y3]
pos5 = [x4,y3]
pos6 = [x5,y3]
pos7 = [x3,y4]
pos8 = [x4,y4]
pos9 = [x5,y4]

#能量花位置
engp  = [258, 789]

#键盘位置
ky = 504
kx = (1024, 161, 261, 361, 452, 552, 652, 739, 832, 927)


##################################################################################
#卡片位置
cardflower1 = [cardx,cardy5]
cardflower2 = [cardx,cardy6]
cardbl = [cardx,cardy8]
cardfog = [cardx,cardy7]

#种花顺序
fstep = [pos7, pos8, pos4, pos9, pos1, pos3, pos2, pos6]

#蓓蕾放置位置
t_beilei = [x2,y4]
#蛙放置位置
t_fog = [x6,y1]

#收能量花路线
energyp = et1

##################################################################################

#create one level , play then del
def createLvl(lname = '1'):
    #点击新建
    c.tap(780, 260)
    time.sleep(0.2)
    #选模式
    c.tap(333, 364)
    time.sleep(0.2)
    #确定
    c.tap(616, 632)
    time.sleep(0.6)

    #点击关闭
    c.tap(1111, 77)
    time.sleep(0.3)

    #选图
    c.tap(367, 267)
    time.sleep(0.2)

    #play
    c.tap(611, 687)

    #等待结算
    time.sleep(8)

    #继续
    c.tap(1061,750)
    time.sleep(5)

    #选图
    c.tap(367, 267)
    time.sleep(0.2)

    #点击改名
    c.tap(930, 208)
    time.sleep(0.3)
    #点击输入框.
    c.tap(333, 294)
    time.sleep(0.2)
    #输入名############
    #切换数字
    c.tap(161, 762)
    time.sleep(0.1)
    for pp in lname:
        c.tap(kx[int(pp)], ky)
    #c.tap(161, 503)
    time.sleep(0.3)
    
    #return
    c.tap(1100, 585)
    time.sleep(0.3)
    #点击确定
    c.tap(613, 434)
    time.sleep(0.3)  

    #点击发布
    c.tap(312, 679)
    time.sleep(0.5)
    #点击确定
    c.tap(490, 600)
    time.sleep(0.3) 
    c.tap(596, 601)
    time.sleep(0.3) 
    #点击关闭
    c.tap(999, 106)
    time.sleep(0.5)

def delLvl(lvlnum=0):
    #点图
    c.tap(373, 279)
    time.sleep(0.3)

    #点删除
    c.tap(495, 426)
    time.sleep(0.3)

    #确定删除
    c.tap(480, 597)
    time.sleep(0.5)

def pingan3():
    #开始战斗
    c.tap(1050,776)

    #等待开始
    time.sleep(7)

    #种花1
    #c.swipe(cardflower1[0], cardflower1[1], step1[0], step1[1], 0.1) # 0.2s
    c.tap(cardflower1[0], cardflower1[1])
    c.tap(fstep[0][0], fstep[0][1])
    #c.swipe(cardflower2[0], cardflower2[1], step2[0], step2[1], 0.1)
    c.tap(cardflower2[0], cardflower2[1])
    c.tap(fstep[1][0], fstep[1][1])
    #种蓓蕾
    #c.swipe(cardbl[0], cardbl[1], t_beilei[0], t_beilei[1], 0.1)
    c.tap(cardbl[0], cardbl[1])
    c.tap(t_beilei[0], t_beilei[1])

    #收阳光
    c.swipe(x1, y3, x5, y3, 0.1)
    c.swipe(x1, y4, x5, y4, 0.1)

    #种花2
    c.tap(1127, 194) #下一波
    #time.sleep(0.3)#等待阳光收集
    c.swipe(cardflower1[0], cardflower1[1], fstep[2][0], fstep[2][1], 0.1) 
    c.swipe(cardflower2[0], cardflower2[1], fstep[3][0], fstep[3][1], 0.1)

    #收阳光
    c.swipe(x1, y4, x5, y4, 0.1)

    #种花3
    time.sleep(0.4)#受植物种植cd影响
    c.swipe(cardflower1[0], cardflower1[1], fstep[4][0], fstep[4][1], 0.1) 
    c.swipe(cardflower2[0], cardflower2[1], fstep[5][0], fstep[5][1], 0.1)

    #收阳光
    c.swipe(x1, y4, x5, y4, 0.1)

    #种花4
    time.sleep(0.3)#受植物种植cd影响
    c.swipe(cardflower1[0], cardflower1[1], fstep[6][0], fstep[6][1], 0.1) 
    c.swipe(cardflower2[0], cardflower2[1], fstep[7][0], fstep[7][1], 0.1)

    #种蛙
    time.sleep(0.3)
    c.swipe(cardfog[0], cardfog[1], t_fog[0], t_fog[1], 0.1)
    
    #收能量豆
    #time.sleep(1)
    c.double_tap(energyp[0],energyp[1])
    c.double_tap(energyp[0],energyp[1])
    c.double_tap(energyp[0],energyp[1])
    c.double_tap(energyp[0],energyp[1])
    c.double_tap(energyp[0],energyp[1])
    c.double_tap(energyp[0],energyp[1])
    c.double_tap(energyp[0],energyp[1])
    c.double_tap(energyp[0],energyp[1])
    #c.tap(1146,48)#暂停确认能量豆位置
    #c.swipe(energyp[0], energyp[1], energytp[0], energytp[1], 1)
    
    #放能量豆
    time.sleep(0.3)
    c.swipe(engp[0], engp[1], pos5[0], pos5[1], 0.1)

    #check (printscreen)
    #picname = "%d.png" % (i)
    #c.screenshot().save(picname)
    #i = i + 1
    time.sleep(2.3)
    #收钱
    c.swipe(x2, y2, x6, y2, 0.1)
    c.swipe(x2, y3, x6, y3, 0.1)
    c.swipe(x2, y4, x6, y4, 0.1)

    #重开
    c.tap(1146,48)#touch((2298,96))/2388 1688
    time.sleep(0.1)
    c.tap(600,630)#touch((1203,1260))
    time.sleep(0.1)
    c.tap(758,580)#touch((1519,1160))
    time.sleep(9)# 

def playList(llist):
    for slvl in llist:
        playLvl(slvl)
   
def playLvl(lvlNum=0):
    #点击游玩
    c.tap(160, 240)
    time.sleep(0.3)

    #点击搜索标签
    c.tap(856, 193)
    time.sleep(0.3)
    #点击文本框
    c.tap(432,254)
    time.sleep(0.3)

    if lvlNum == 0:
        #粘贴
        c.tap(126,429)
        time.sleep(0.2)
    else:
        #切换数字
        c.tap(161, 762)
        time.sleep(0.1)
        for pp in str(lvlNum):
            c.tap(kx[int(pp)], ky)
    #点击搜索按钮
    c.tap(995, 250)
    time.sleep(0.5)

    #点图
    c.tap(384, 363)
    time.sleep(0.4)

    #挑战
    c.tap(600, 682)

    #等待结算
    time.sleep(8.2)

    #点赞
    c.tap(506, 552)
    time.sleep(0.4)

    #继续
    c.tap(1050,750)

    #等待加载
    time.sleep(5)

def createTmbDel(counts = 31):
    for num in range(1,counts):
        lname = str(num)
        #创建
        createLvl(lname = lname)
        #游玩点赞
        playLvl(0)
        #删除
        delLvl(0)

        print(lname + "  ---  " + time.strftime("%H:%M:%S"))

def main():
    #createTmbDel(31)
    #llist = [490345, 490363, 490539, 490528, 490563, 490594, 490755, 490841, 490857, 490862, 490867, 491040, 491062, 491081, 491102, 491291, 491311, 491324, 491351, 491370]
    
    llist = [505677, 505723,505888,505957,506136,506206,506371,506417,506485,506663, \
             100433,101236 ,102179 ,102476 ,117035, 117105, 117533 ,117625 ,280849, 281091 ]
    playList(llist)

main()


