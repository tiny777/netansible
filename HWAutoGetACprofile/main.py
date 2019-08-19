#!/usr/bin/env python
#coding=utf-8
from netmiko import Netmiko
from netmiko import ConnectHandler
import time
import re
import pandas as pd

def sshLogin(hostName,userName,timeNow):
    # make a struct that include the host's information to auto ssh login
    hw_device = {
    'device_type':'huawei',
    'host':hostName,
    'username':userName,
    'password':passWord
    }
    # get the whitelist-profile name and then splice them into the final command
    profileName = 'display sta-whitelist-profile name ' + input("请输入whitelist-profile name： ")
    
    # using ssh to login the target host
    net_connect = ConnectHandler(**hw_device)
    # set the commands that need to be executed after login
    config_commands = ['system-view', 'wlan', profileName]
    # excute the commands
    output = net_connect.send_config_set(config_commands)
    # print all the process and Results
    print(output)

    # log all the process and Results
    with open('debug.log', 'a+',encoding='utf-8') as f:    
            f.write('\n\n--------------------------------------------------\n')
            f.write('--------------------------------------------------\n')
            f.write(timeNow)
            f.write(',')
            f.write(hostName)
            f.write(',')
            f.write(userName)
            f.write('\n--------------------------------------------------\n')
            f.write(output)
            f.write('\n--------------------------------------------------\n')
            f.write('--------------------------------------------------\n\n')
            # display the dividing line to split display area
            print ("\n\n--------------------------------------------------")
            print('Finish logging')
            print ("--------------------------------------------------\n\n")
            

    # write all the process and Results into cache file
    with open('./cache/Cache-' + hostName + '-' + timeNow,'w',encoding='utf-8') as f:
            f.write(output)
            # display the dividing line to split display area
            print ("\n\n--------------------------------------------------")
            print('Finish writing cache')
            print ("--------------------------------------------------\n\n")

    # disconnect with host
    net_connect.disconnect()

def sort_to_csv(hostName,timeNow):
    # Specify the encoding format as utf-8 to support Chinese characters
    with open('./cache/Cache-' + hostName + '-' + timeNow,'r',encoding='utf-8') as fr,\
        open('./csv/Result-' + hostName + '-' + timeNow + '.csv','w',encoding='utf-8') as fw:
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
    print ("\n\n--------------------------------------------------")
    print('Finish changing cache to csv')
    print ("--------------------------------------------------\n\n")

def csv_to_xlsx_pd(hostName,timeNow):
    csv = pd.read_csv('./csv/Result-' + hostName + '-' + timeNow + '.csv', header=None, encoding='utf-8')
    #csv.columns = ['No.', 'MAC', 'Description']
    #csv.columns = ['No.', 'MAC']
    csv.to_excel('./excel/Result-' + hostName + '-' + timeNow + '.xlsx' , sheet_name = timeNow, index = None, header=None, encoding = 'utf-8')
    print ("\n\n--------------------------------------------------")
    print('Finish changing csv to excel')
    print ("--------------------------------------------------\n\n")

if __name__ == '__main__':
    # get the current time to log
    timeNow = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))

    # get host's information to login
    print ("\n\n--------------------------------------------------\n")
    hostName = input("请输入主机名或IP： ")
    userName = input("请输入用户名    ： ")
    passWord = input("请输入密码      ： ")
    print ("\n--------------------------------------------------\n\n")

    # print all the information that user entered
    print ("\n\n--------------------------------------------------\n")
    print ("您输入的主机名或IP是: ", hostName)
    print ("您输入的用户名是    : ", userName)
    print ("您输入的密码是      : ", passWord)
    print ("\n--------------------------------------------------\n\n")

    sshLogin(hostName,userName,timeNow)    
    sort_to_csv(hostName,timeNow)
    csv_to_xlsx_pd(hostName,timeNow)
    