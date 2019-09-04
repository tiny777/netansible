#!/usr/bin/env python
#coding=utf-8
from netmiko import SSHDetect,Netmiko
from netmiko import ConnectHandler
from multiprocessing import Pool
from multiprocessing import cpu_count
import os, time, random
import time
import re
import pandas as pd
import os
import _thread
import threading
import multiprocessing


def makeDir(dirs):
    if not os.path.exists(dirs):
        os.makedirs(dirs)
        print ("\n--------------------------------------------------------")
        print ( "目录" + dirs + "不存在，已成功创建")
        print ("--------------------------------------------------------\n")

def excCom(net_connect,netCommand):
    output = net_connect.send_command_timing(netCommand)
    print(output)
    with open('debug.log', 'a+',encoding='utf-8') as f:    
            f.write('\n--------------------------------------------------------\n')
            f.write(output)
            f.write('\n--------------------------------------------------------\n')

def sshLogin(timeNow,hostName,userName,passWord):
    # make a struct that include the host's information to auto ssh login
    deviceType = 'cisco_ios'
    # hostName = "192.168.195.2"
    # userName = "tinychen"
    # passWord = "easy1234"

    device = {
    'device_type':deviceType,
    'host':hostName,
    'username':userName,
    'password':passWord
    }

    #print ("\n--------------------------------------------------------")
    #print ("正在检测设备类型并尝试建立SSH连接，请稍候……")
    #print ("--------------------------------------------------------\n")

    # auto detect the device's type
    # Name of the best device_type to use further
    #guesser = SSHDetect(**device)
    # Dictionary of the whole matching result
    #deviceType = guesser.autodetect()
    #print (deviceType)
    # write device's basic info into log file
    with open('debug.log', 'a+',encoding='utf-8') as f:    
            f.write('\n\n\n--------------------------------------------------------\n')
            f.write('--------------------------------------------------------\n')
            f.write(timeNow)
            f.write(',')
            f.write(hostName)
            f.write(',')
            f.write(userName)
            f.write(',')
            f.write(deviceType)
            f.write(',')
            f.write(str(deviceType))
            f.write('\n--------------------------------------------------------\n')  
    
    # using ssh to login the target host
    net_connect = ConnectHandler(**device)
    #print ("\n--------------------------------------------------------")
    #print ("主机连接成功,设备类型为"+str(guesser.potential_matches))
    #print ("--------------------------------------------------------\n")



    '''
    # set the commands that need to be executed after login
    with open('D:\\GitHub\\netansible\\Codes\\command', 'r',encoding='utf-8') as f:  
        for netCommand in f:
            #print (netCommand.strip('\n'))
            excCom(net_connect,netCommand.strip('\n'))
    '''
    #excCom(net_connect,"terminal length 0")
    print ("\n--------------------------------------------------------\n" + hostName + " " + userName + " " + deviceType + "\n" + net_connect.send_command_timing("sh ip int brief") + "\n--------------------------------------------------------\n")
    #excCom(net_connect,"sh ip int brief")
    # disconnect with host
    net_connect.disconnect()

if __name__ == '__main__':
    # get the current time to log
    timeNow = time.strftime('%Y%m%d-%H%M%S',time.localtime(time.time()))
    '''
    sshLogin(timeNow,'192.168.126.5','tinychen','easy1234')
    sshLogin(timeNow,'192.168.126.6','tinychen','easy1234')
    sshLogin(timeNow,'192.168.126.7','tinychen','easy1234')
    sshLogin(timeNow,'192.168.126.8','tinychen','easy1234')
    sshLogin(timeNow,'192.168.126.9','tinychen','easy1234')
    sshLogin(timeNow,'192.168.126.10','tinychen','easy1234')
    '''
    #sshLogin(timeNow,'192.168.195.2','tinychen','easy1234','netcommand2')

    '''
    # This code uses thread lib to implement multithreading.
    try:
        _thread.start_new_thread( sshLogin, (timeNow,'192.168.195.2','tinychen','easy1234','netcommand2') )
        _thread.start_new_thread( sshLogin, (timeNow,'192.168.195.3','tinychen','easy1234','netcommand2') )
    except:
        print ("Error: 无法启动线程")
    
    while 1:
        pass

    '''

    '''
    # This code uses threading lib to implement multithreading.
    class myThread (threading.Thread):
        def __init__(self, threadID, name, ip):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.ip = ip
        def run(self):
            #print ("开始线程：" + self.name)
            # lock thread to sync
            threadLock.acquire()
            sshLogin(timeNow,self.ip,'tinychen','easy1234')
            # unlock thread and start next thread
            threadLock.release()
            #print ("退出线程：" + self.name)

    threadLock = threading.Lock()
    threads = []
    thread1 = myThread(1, "Thread-192.168.126.5", "192.168.126.5")
    thread2 = myThread(2, "Thread-192.168.126.6", "192.168.126.6")
    thread3 = myThread(3, "Thread-192.168.126.7", "192.168.126.7")
    thread4 = myThread(4, "Thread-192.168.126.8", "192.168.126.8")
    thread5 = myThread(5, "Thread-192.168.126.9", "192.168.126.9")
    thread6 = myThread(6, "Thread-192.168.126.10", "192.168.126.10")

    # start new thread
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    #print ("退出主线程")
    '''



    mp1 = multiprocessing.Process(target=sshLogin,args=(timeNow,'192.168.126.5','tinychen','easy1234',))
    mp2 = multiprocessing.Process(target=sshLogin,args=(timeNow,'192.168.126.6','tinychen','easy1234',))
    mp3 = multiprocessing.Process(target=sshLogin,args=(timeNow,'192.168.126.7','tinychen','easy1234',))
    mp4 = multiprocessing.Process(target=sshLogin,args=(timeNow,'192.168.126.8','tinychen','easy1234',))
    mp5 = multiprocessing.Process(target=sshLogin,args=(timeNow,'192.168.126.9','tinychen','easy1234',))
    mp6 = multiprocessing.Process(target=sshLogin,args=(timeNow,'192.168.126.10','tinychen','easy1234',))
    mp1.start()

    mp2.start()

    mp3.start()

    mp4.start()

    mp5.start()

    mp6.start()
    #mp2.join()
    '''
    pool = multiprocessing.Pool(processes=cpu_count())

    print(cpu_count())
    print('Parent process %s.' % os.getpid())
    p = Pool(cpu_count())
    p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
    '''

    '''
    print ("\n--------------------------------------------------------")
    print ("请按任意键退出……")
    print ("--------------------------------------------------------\n")
    endstr = input()
    print (" ")
    '''