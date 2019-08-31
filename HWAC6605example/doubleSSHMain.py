#!/usr/bin/env python
#coding=utf-8
from netmiko import SSHDetect,Netmiko
from netmiko import ConnectHandler
import time
import re
import pandas as pd
import os

def makeDir(dirs):
    if not os.path.exists(dirs):
        os.makedirs(dirs)
        print ("\n--------------------------------------------------------")
        print ( "目录" + dirs + "不存在，已成功创建")
        print ("--------------------------------------------------------\n")

def sshLogin(hostName,userName,timeNow,passWord,hostName2,userName2,password2):
    # make a struct that include the host's information to auto ssh login
    deviceType = 'autodetect'
    device = {
    'device_type':deviceType,
    #'device_type':'huawei_vrpv8',
    'host':hostName,
    'username':userName,
    'password':passWord
    }
    # get the whitelist-profile name and then splice them into the final command
    print ("\n--------------------------------------------------------")
    profileName = 'display sta-whitelist-profile name ' + input("请输入whitelist-profile name： ")
    print ("--------------------------------------------------------\n")
    #profileName = 'display sta-whitelist-profile name staff-devp'

    print ("\n--------------------------------------------------------")
    print ("正在尝试连接第一台主机，请稍候……")
    print ("--------------------------------------------------------\n")

    guesser = SSHDetect(**device)
    deviceType = guesser.autodetect()
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
            f.write(str(guesser.potential_matches))
            f.write('\n--------------------------------------------------------\n')
    print(deviceType)                   # Name of the best device_type to use further
    print(guesser.potential_matches)    # Dictionary of the whole matching result
    # using ssh to login the target host
    net_connect = ConnectHandler(**device)
    net_connect.send_command_timing('n')
    print ("\n--------------------------------------------------------")
    print ("第一台主机连接成功，正在尝试连接第二台主机，请稍候……")
    print ("--------------------------------------------------------\n")

    # set the commands that need to be executed after login
    stelnetHost2 = 'stelnet ' + hostName2
    #config_commands1 = ['system', stelnetHost2,userName2]
    # excute the commands
    #output1 = net_connect.send_config_set(config_commands1)
    #print(output1)
    allOutput = '\n'

    output = net_connect.send_command_timing('system-view')
    print(output)
    allOutput = allOutput + '\n' + output

    output = net_connect.send_command_timing(stelnetHost2) 
    print(output)
    allOutput = allOutput + '\n' + output
    
    net_connect.send_command_timing('y')
    net_connect.send_command_timing('n')

    output = net_connect.send_command_timing(userName2) 
    print(output)
    allOutput = '\n'
    allOutput = allOutput + '\n' + output

    output = net_connect.send_command_timing(passWord2) 
    print(output)
    allOutput = allOutput + '\n' + output

    output = net_connect.send_command_timing('screen-length 0 temporary')
    print(output)
    allOutput = allOutput + '\n' + output

    output = net_connect.send_command_timing('system-view')
    print(output)
    allOutput = allOutput + '\n' + output

    output = net_connect.send_command_timing('wlan')
    print(output)
    allOutput = allOutput + '\n' + output
    
    output = net_connect.send_command_timing(profileName)
    print(output)
    allOutput = allOutput + '\n' + output
    
    '''
    i = 0
    while i < 3 :
        output = net_connect.send_command_timing('')
        i = i+1
        print(output)
        allOutput = allOutput + '\n' + output
    '''
    # print all the process and Results
    #output = output1 + '\n' + output2 + '\n' + output4 + '\n' + output5 + '\n' + output6

    # log all the process and Results
    with open('debug.log', 'a+',encoding='utf-8') as f:    
            f.write('\n--------------------------------------------------------\n')
            f.write(allOutput)
            f.write('\n--------------------------------------------------------\n')
            f.write('--------------------------------------------------------\n')
            # display the dividing line to split display area
            print ("\n--------------------------------------------------------")
            print ('log日志写入完成，文件位于根目录下')
            print ("--------------------------------------------------------\n")
            
    makeDir('./cache/')
    # write all the process and Results into cache file
    with open('./cache/' + hostName2 + '-' + timeNow,'w',encoding='utf-8') as f:
            f.write(allOutput)
            # display the dividing line to split display area
            print ("\n--------------------------------------------------------")
            print ('cache写入完成，文件位于cache目录下')
            print ("--------------------------------------------------------\n")

    # disconnect with host
    net_connect.disconnect()

def sort_to_csv(hostName,timeNow):
    print ("\n--------------------------------------------------------")
    print ('开始将cache转为csv')
    print ("--------------------------------------------------------\n")
    makeDir('./cache/')
    makeDir('./csv/')
    # Specify the encoding format as utf-8 to support Chinese characters
    with open('./cache/' + hostName + '-' + timeNow,'r',encoding='utf-8') as fr,\
        open('./csv/' + hostName + '-' + timeNow + '.csv','w',encoding='utf-8') as fw:
        for line in fr.readlines():
            # use lstrip to delete the empty space at the beginning of the line
            line = line.lstrip()
            # use re.match to match rows with numbers at the beginning of the line
            matchObj = re.match( r'[0-9]',line)
            if matchObj:
                # use split() to delete multiple space and then use join and , to separate the string
                line=','.join(line.split())
                # print the matched and processed strings
                print (line)
                # write the strings into csv file
                fw.write(line +'\n')
    print ("\n--------------------------------------------------------")
    print ('cache转csv操作完成，文件位于csv目录下')
    print ("--------------------------------------------------------\n")

def csv_to_xlsx_pd(hostName,timeNow):
    print ("\n--------------------------------------------------------")
    print ('开始将csv转为excel')
    print ("--------------------------------------------------------\n")
    makeDir('./excel/')
    makeDir('./csv/')    
    csv = pd.read_csv('./csv/' + hostName + '-' + timeNow + '.csv', header=None, encoding='utf-8')
    #csv.columns = ['No.', 'MAC', 'Description']
    #csv.columns = ['No.', 'MAC']
    csv.to_excel('./excel/' + hostName + '-' + timeNow + '.xlsx' , sheet_name = timeNow, index = None, header=None, encoding = 'utf-8')
    print ("\n--------------------------------------------------------")
    print ('csv转为excel操作完成，文件位于excel目录下')
    print ("--------------------------------------------------------\n")

if __name__ == '__main__':
    # get the current time to log
    timeNow = time.strftime('%Y%m%d-%H%M%S',time.localtime(time.time()))

    # get the first host's information to login
    print ("\n--------------------------------------------------------")
    hostName = input("请输入第一台SSH的设备IP    ： ")
    userName = input("请输入第一台SSH的设备用户名： ")
    passWord = input("请输入第一台SSH的设备密码  ： ")
    print ("--------------------------------------------------------\n")

    # get the second host's information to login
    print ("\n--------------------------------------------------------")
    hostName2 = input("请输入第二台SSH的设备IP    ： ")
    userName2 = input("请输入第二台SSH的设备用户名： ")
    passWord2 = input("请输入第二台SSH的设备密码  ： ")
    print ("--------------------------------------------------------\n")


    sshLogin(hostName,userName,timeNow,passWord,hostName2,userName2,passWord2)    
    sort_to_csv(hostName2,timeNow)
    csv_to_xlsx_pd(hostName2,timeNow)

    print ("\n--------------------------------------------------------")
    print ("请按任意键退出……")
    print ("--------------------------------------------------------\n")
    endstr = input()
    print ("--------------------------------------------------------\n")