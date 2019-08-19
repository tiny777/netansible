#!/usr/bin/python
#coding=utf-8

import paramiko

# create an ssh object
ssh = paramiko.SSHClient()

# add the server into the known_hosts files
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


# connect to the server
hostName = input("请输入主机名或IP：")
print ("您输入的主机名或IP是: ", hostName)

sshPort = input("请输入ssh端口号（默认为22）：")
print ("您输入的ssh端口号是: ", sshPort)

userName = input("请输入用户名：")
print ("您输入的用户名是: ", userName)

passWord = input("请输入密码：")
print ("您输入的密码是: ", passWord)

ssh.connect(hostname = hostName, port = sshPort, username = userName, password = passWord, )


# cmd = 'ps -aux'

# use ; to separate multiple commands
cmd = 'ls -l;ifconfig'     
# cmd = 'help'
stdin, stdout, stderr = ssh.exec_command(cmd)

result = stdout.read()

if not result:
    result = stderr.read()
ssh.close()

print(result.decode())