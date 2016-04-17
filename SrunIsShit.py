__author__ = 'Eason Yang'

import network
import task
import kill
import restart
import time

while 1 :
    if 22 == time.localtime(time.time()).tm_hour and 40 <= time.localtime(time.time()).tm_min and 40 <= time.localtime(time.time()).tm_min :
        specialTime = False
        timeNotify = True
    else :
        specialTime = True
        timeNotify = False
    if task.checkProcess() :
        if specialTime :
            timeNotify = False
        while 1 :
            if network.testNetwork('http://nss.hrbeu.edu.cn') :
                time.sleep(3)
                continue
            elif network.testNetwork('http://cn.bing.com') :
                break
            else :
                time.sleep(3)
                pidList = task.getPid()
                for item in pidList :
                    kill.killTask(item)
                if timeNotify :
                    specialTime = True
                    break
                else :
                    restart.restart()
    else :
        time.sleep(30)