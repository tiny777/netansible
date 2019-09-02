## 网络拓扑
这里我们使用桥接模式，直接将GNS3中的虚拟网络设备和真机网卡进行桥接，由于只是用于测试ssh，不需要进行其他复杂的网络拓扑配置，只需要保证能ping通即可。后面创建的四台c3725是用于之后的批量ssh测试的。
![mark](http://qiniuyun.tiny777.com/blog/20190902/K7gUudKtt4dB.png)

## 配置命令

```
# 查看端口的ip和状态
show ip int brief

# 进入配置命令行模式
conf t

# 进入某个特定端口
int f0/0

# 配置ip地址
ip address $ip $mask

# 开启端口
no shut

# 配置hostname
hostname $hostname

# 配置domain-name
ip domain-name $domain-name

# 生成1024位的密钥，密钥长度范围为360-2048
crypto key generate rsa general-keys modulus 1024

# 配置所使用的SSH版本为2
ip ssh version 2

# 配置SSH会话的超时时间为2分钟（120秒）
ip ssh time-out 120

# 配置SSH认证的最大次数为3
ip ssh authentication-retries 3

# 启用SSH认证：
line vty 0 4
transport input ssh

# 使用用户名+密码登录认证
login local 

# 创建本地ssh用户
username $username password $password

```

## C7200配置ip和ssh

### 配置过程
```
c7200#
c7200#sh ip int brief
Interface              IP-Address      OK? Method Status                Protocol
FastEthernet0/0        unassigned      YES unset  administratively down down
FastEthernet2/0        unassigned      YES unset  administratively down down
FastEthernet3/0        unassigned      YES unset  administratively down down
FastEthernet3/1        unassigned      YES unset  administratively down down
GigabitEthernet4/0     unassigned      YES unset  administratively down down
Serial5/0              unassigned      YES unset  administratively down down
Serial5/1              unassigned      YES unset  administratively down down
Serial5/2              unassigned      YES unset  administratively down down
Serial5/3              unassigned      YES unset  administratively down down
Serial5/4              unassigned      YES unset  administratively down down
Serial5/5              unassigned      YES unset  administratively down down
Serial5/6              unassigned      YES unset  administratively down down
Serial5/7              unassigned      YES unset  administratively down down
Ethernet6/0            unassigned      YES unset  administratively down down
Ethernet6/1            unassigned      YES unset  administratively down down
Ethernet6/2            unassigned      YES unset  administratively down down
Ethernet6/3            unassigned      YES unset  administratively down down
c7200#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
c7200(config)#int g4/0
c7200(config-if)#ip address 192.168.126.5 255.255.255.0
c7200(config-if)#no shut
c7200(config-if)#
*Sep  2 10:09:34.459: %LINK-3-UPDOWN: Interface GigabitEthernet4/0, changed state to up
c7200(config-if)#
*Sep  2 10:09:35.459: %LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet4/0, changed state to up
c7200(config-if)#exit
c7200(config)#hostname c7200-5
c7200-5(config)#ip domain-name tinychen.com
c7200-5(config)#crypto key generate rsa general-keys modulus 1024
The name for the keys will be: c7200-5.tinychen.com

% The key modulus size is 1024 bits
% Generating 1024 bit RSA keys, keys will be non-exportable...
[OK] (elapsed time was 1 seconds)

c7200-5(config)#
*Sep  2 10:11:12.303: %SSH-5-ENABLED: SSH 1.99 has been enabled
c7200-5(config)#ip ssh version 2
c7200-5(config)#ip ssh time-out 120
c7200-5(config)#ip ssh authentication-retries 3
c7200-5(config)#line vty 0 4
c7200-5(config-line)#transport input ssh
c7200-5(config-line)#login local
c7200-5(config-line)#exit
c7200-5(config)#username tinychen password easy1234
c7200-5(config)#exit
c7200-5#
*Sep  2 10:12:39.903: %SYS-5-CONFIG_I: Configured from console by console
c7200-5#sh ip int brief
Interface              IP-Address      OK? Method Status                Protocol
FastEthernet0/0        unassigned      YES unset  administratively down down
FastEthernet2/0        unassigned      YES unset  administratively down down
FastEthernet3/0        unassigned      YES unset  administratively down down
FastEthernet3/1        unassigned      YES unset  administratively down down
GigabitEthernet4/0     192.168.126.5   YES manual up                    up
Serial5/0              unassigned      YES unset  administratively down down
Serial5/1              unassigned      YES unset  administratively down down
Serial5/2              unassigned      YES unset  administratively down down
Serial5/3              unassigned      YES unset  administratively down down
Serial5/4              unassigned      YES unset  administratively down down
Serial5/5              unassigned      YES unset  administratively down down
Serial5/6              unassigned      YES unset  administratively down down
Serial5/7              unassigned      YES unset  administratively down down
Ethernet6/0            unassigned      YES unset  administratively down down
Ethernet6/1            unassigned      YES unset  administratively down down
Ethernet6/2            unassigned      YES unset  administratively down down
Ethernet6/3            unassigned      YES unset  administratively down down
c7200-5#
```



### 登录测试
![mark](http://qiniuyun.tiny777.com/blog/20190902/0edK3bDVbndR.png)


## C3725配置ip和ssh

### 配置过程
```
c3725#
c3725#sh ip int br
Interface              IP-Address      OK? Method Status                Protocol
FastEthernet0/0        unassigned      YES unset  administratively down down
FastEthernet2/0        unassigned      YES unset  administratively down down
FastEthernet3/0        unassigned      YES unset  administratively down down
FastEthernet3/1        unassigned      YES unset  administratively down down
GigabitEthernet4/0     unassigned      YES unset  administratively down down
Serial5/0              unassigned      YES unset  administratively down down
Serial5/1              unassigned      YES unset  administratively down down
Serial5/2              unassigned      YES unset  administratively down down
Serial5/3              unassigned      YES unset  administratively down down
Serial5/4              unassigned      YES unset  administratively down down
Serial5/5              unassigned      YES unset  administratively down down
Serial5/6              unassigned      YES unset  administratively down down
Serial5/7              unassigned      YES unset  administratively down down
Ethernet6/0            unassigned      YES unset  administratively down down
Ethernet6/1            unassigned      YES unset  administratively down down
Ethernet6/2            unassigned      YES unset  administratively down down
Ethernet6/3            unassigned      YES unset  administratively down down
c3725#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
c3725(config)#int g4/0
c3725(config-if)#ip address 192.168.126.6 255.255.255.0
c3725(config-if)#exit
c3725(config)#hostname c3725-6
c3725-6(config)#ip domai
c3725-6(config)#ip domain-na
c3725-6(config)#ip domain-name tinychen.com
c3725-6(config)#crypto key generate rsa general-keys modulus 1024
The name for the keys will be: c3725-6.tinychen.com

% The key modulus size is 1024 bits
% Generating 1024 bit RSA keys, keys will be non-exportable...
[OK] (elapsed time was 0 seconds)

c3725-6(config)#
*Sep  2 10:20:22.999: %SSH-5-ENABLED: SSH 1.99 has been enabled
c3725-6(config)#ip ssh version 2
c3725-6(config)#ip ssh time-out 120
c3725-6(config)#ip ssh authentication-retries 3
c3725-6(config)#line vty 0 4
c3725-6(config-line)#transport input ssh
c3725-6(config-line)#login local
c3725-6(config-line)#exit
c3725-6(config)#username tinychen password easy1234
c3725-6(config)#int g4/0
c3725-6(config-if)#no shutdown
c3725-6(config-if)#
*Sep  2 10:22:02.275: %LINK-3-UPDOWN: Interface GigabitEthernet4/0, changed state to up
*Sep  2 10:22:03.275: %LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet4/0, changed state to up
c3725-6(config-if)#e
c3725-6(config)#exit
*Sep  2 10:22:10.355: %SYS-5-CONFIG_I: Configured from console by console
c3725-6#sh ip int brief
Interface              IP-Address      OK? Method Status                Protocol
FastEthernet0/0        unassigned      YES unset  administratively down down
FastEthernet2/0        unassigned      YES unset  administratively down down
FastEthernet3/0        unassigned      YES unset  administratively down down
FastEthernet3/1        unassigned      YES unset  administratively down down
GigabitEthernet4/0     192.168.126.6   YES manual up                    up
Serial5/0              unassigned      YES unset  administratively down down
Serial5/1              unassigned      YES unset  administratively down down
Serial5/2              unassigned      YES unset  administratively down down
Serial5/3              unassigned      YES unset  administratively down down
Serial5/4              unassigned      YES unset  administratively down down
Serial5/5              unassigned      YES unset  administratively down down
Serial5/6              unassigned      YES unset  administratively down down
Serial5/7              unassigned      YES unset  administratively down down
Ethernet6/0            unassigned      YES unset  administratively down down
Ethernet6/1            unassigned      YES unset  administratively down down
Ethernet6/2            unassigned      YES unset  administratively down down
Ethernet6/3            unassigned      YES unset  administratively down down
c3725-6#
```



### 测试效果

![mark](http://qiniuyun.tiny777.com/blog/20190902/IW9ChzJV5FgL.png)


## C3745配置ip和ssh

### 配置过程

```
c3745#sh ip int br
Interface                  IP-Address      OK? Method Status                Protocol
FastEthernet0/0            unassigned      YES unset  administratively down down
Serial0/0                  unassigned      YES unset  administratively down down
FastEthernet0/1            unassigned      YES unset  administratively down down
Serial0/1                  unassigned      YES unset  administratively down down
Serial0/2                  unassigned      YES unset  administratively down down
Serial0/3                  unassigned      YES unset  administratively down down
FastEthernet1/0            unassigned      YES unset  administratively down down
Serial2/0                  unassigned      YES unset  administratively down down
Serial2/1                  unassigned      YES unset  administratively down down
Serial2/2                  unassigned      YES unset  administratively down down
Serial2/3                  unassigned      YES unset  administratively down down
FastEthernet3/0            unassigned      YES unset  up                    down
FastEthernet3/1            unassigned      YES unset  up                    down
FastEthernet3/2            unassigned      YES unset  up                    down
FastEthernet3/3            unassigned      YES unset  up                    down
FastEthernet3/4            unassigned      YES unset  up                    down
FastEthernet3/5            unassigned      YES unset  up                    down
FastEthernet3/6            unassigned      YES unset  up                    down
FastEthernet3/7            unassigned      YES unset  up                    down
FastEthernet3/8            unassigned      YES unset  up                    down
FastEthernet3/9            unassigned      YES unset  up                    down
FastEthernet3/10           unassigned      YES unset  up                    down
FastEthernet3/11           unassigned      YES unset  up                    down
FastEthernet3/12           unassigned      YES unset  up                    down
FastEthernet3/13           unassigned      YES unset  up                    down
FastEthernet3/14           unassigned      YES unset  up                    down
FastEthernet3/15           unassigned      YES unset  up                    down
Vlan1                      unassigned      YES unset  up                    down
c3745#
c3745#
c3745#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
c3745(config)#hostname c3745-7
c3745-7(config)#int f0/0
c3745-7(config-if)#ip address 192.168.126.7 255.255.255.0
c3745-7(config-if)#no shutdown
c3745-7(config-if)#exit
c3745-7(config)#
*Mar  1 00:32:35.079: %LINK-3-UPDOWN: Interface FastEthernet0/0, changed state to up
*Mar  1 00:32:36.079: %LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/0, changed state to up
c3745-7(config)#ip domain-name tinychen.com
c3745-7(config)#crypto key generate rsa general-keys modulus 1024
The name for the keys will be: c3745-7.tinychen.com
```

% The key modulus size is 1024 bits
% Generating 1024 bit RSA keys, keys will be non-exportable...[OK]

c3745-7(config)#
*Mar  1 00:34:38.831: %SSH-5-ENABLED: SSH 1.99 has been enabled
c3745-7(config)#ip ssh version 2
c3745-7(config)#ip ssh time-out 120
c3745-7(config)#ip ssh authentication-retries 3
c3745-7(config)#line vty 0 4
c3745-7(config-line)#transport input ssh
c3745-7(config-line)#login local
c3745-7(config-line)#userna
c3745-7(config-line)#exit
c3745-7(config)#username tinychen password easy1234
c3745-7(config)#exit
c3745-7#
*Mar  1 00:35:59.739: %SYS-5-CONFIG_I: Configured from console by console
c3745-7#




### 测试效果
![mark](http://qiniuyun.tiny777.com/blog/20190902/y9CbqfcFsPH5.png)

随后我们用相同的命令不同的ip来配置c3745-8、c3745-9和c3745-10三台设备。
![mark](http://qiniuyun.tiny777.com/blog/20190902/s19iKcYf020N.png)