## 华为AC6605

### 配置IP地址

```
<AC6005>
<AC6005>sys
Enter system view, return user view with Ctrl+Z.
[AC6005]vlan 10
[AC6005-vlan10]q
[AC6005]int Vlanif 10
[AC6005-Vlanif10]ip address 192.168.126.2 24
[AC6005-Vlanif10]q
[AC6005]int GigabitEthernet 0/0/1
[AC6005-GigabitEthernet0/0/1]port link-type access 
[AC6005-GigabitEthernet0/0/1]port default vlan 10
[AC6005-GigabitEthernet0/0/1]ping 192.168.126.1
  PING 192.168.126.1: 56  data bytes, press CTRL_C to break
    Reply from 192.168.126.1: bytes=56 Sequence=1 ttl=128 time=400 ms
    Reply from 192.168.126.1: bytes=56 Sequence=2 ttl=128 time=450 ms
    Reply from 192.168.126.1: bytes=56 Sequence=3 ttl=128 time=360 ms
    Reply from 192.168.126.1: bytes=56 Sequence=4 ttl=128 time=450 ms
    Reply from 192.168.126.1: bytes=56 Sequence=5 ttl=128 time=350 ms

  --- 192.168.126.1 ping statistics ---
    5 packet(s) transmitted
    5 packet(s) received
    0.00% packet loss
    round-trip min/avg/max = 350/402/450 ms

[AC6005-GigabitEthernet0/0/1]q
[AC6005]q
<AC6005>save
  The current configuration will be written to the device. 
  Are you sure to continue? (y/n)[n]:y
  It will take several minutes to save configuration file, please wait......
  Configuration file had been saved successfully
  Note: The configuration file will take effect after being activated
```



### 配置SSH服务

```
<AC6005>sys
Enter system view, return user view with Ctrl+Z.
[AC6005]rsa local-key-pair create
The key name will be: Host
% RSA keys defined for Host already exist.
Confirm to replace them? (y/n)[n]:y
The range of public key size is (512 ~ 2048).
NOTES: If the key modulus is greater than 512,
       It will take a few minutes.
Input the bits in the modulus[default = 2048]:
Generating keys...
.........................+++
..........................................+++
.....++++++++
..........++++++++

[AC6005]stelnet server enable
Info: Succeeded in starting the STELNET server.
[AC6005]user-interface vty 0 4
[AC6005-ui-vty0-4]authentication-mode aaa
[AC6005-ui-vty0-4]protocol inbound ssh
[AC6005-ui-vty0-4]q
[AC6005]aaa
[AC6005-aaa]local-user tinychen password irreversible-cipher easy1234
Info: Add a new user.
[AC6005-aaa]local-user tinychen privilege level 3
[AC6005-aaa]local-user tinychen service-type ssh
[AC6005-aaa]q
[AC6005]ssh user tinychen authentication-type password
 Authentication type setted, and will be in effect next time
[AC6005]q
<AC6005>save
  The current configuration will be written to the device. 
  Are you sure to continue? (y/n)[n]:y
  It will take several minutes to save configuration file, please wait......
  Configuration file had been saved successfully
  Note: The configuration file will take effect after being activated
```



## 华为AR2240

### 配置IP地址

```
The device is running!

<Huawei>sys
Enter system view, return user view with Ctrl+Z.
[Huawei]interface GigabitEthernet 0/0/0
[Huawei-GigabitEthernet0/0/0]ip address 192.168.126.3 24
Aug 31 2019 20:13:06-08:00 Huawei %%01IFNET/4/LINK_STATE(l)[0]:The line protocol
 IP on the interface GigabitEthernet0/0/0 has entered the UP state. 
[Huawei-GigabitEthernet0/0/0]ping 192.168.126.1
  PING 192.168.126.1: 56  data bytes, press CTRL_C to break
    Reply from 192.168.126.1: bytes=56 Sequence=1 ttl=128 time=40 ms
    Reply from 192.168.126.1: bytes=56 Sequence=2 ttl=128 time=10 ms
    Reply from 192.168.126.1: bytes=56 Sequence=3 ttl=128 time=20 ms
    Reply from 192.168.126.1: bytes=56 Sequence=4 ttl=128 time=10 ms
    Reply from 192.168.126.1: bytes=56 Sequence=5 ttl=128 time=10 ms

  --- 192.168.126.1 ping statistics ---
    5 packet(s) transmitted
    5 packet(s) received
    0.00% packet loss
    round-trip min/avg/max = 10/18/40 ms

[Huawei-GigabitEthernet0/0/0]q
[Huawei]q
<Huawei>save
  The current configuration will be written to the device. 
  Are you sure to continue? (y/n)[n]:y
  It will take several minutes to save configuration file, please wait.......
  Configuration file had been saved successfully
  Note: The configuration file will take effect after being activated
```

### 配置SSH服务
```
<Huawei>system-view 
Enter system view, return user view with Ctrl+Z.
[Huawei]rsa local-key-pair create
The key name will be: Host
% RSA keys defined for Host already exist.
Confirm to replace them? (y/n)[n]:y
The range of public key size is (512 ~ 2048).
NOTES: If the key modulus is greater than 512,
       It will take a few minutes.
Input the bits in the modulus[default = 512]:
Generating keys...
......++++++++++++
...++++++++++++
.........++++++++
..........++++++++

[Huawei]stelnet server enable
Info: Succeeded in starting the STELNET server.
[Huawei]user-interface vty 0 4
[Huawei-ui-vty0-4]authentication-mode aaa
[Huawei-ui-vty0-4]protocol inbound ssh
[Huawei-ui-vty0-4]q
[Huawei]aaa
[Huawei-aaa]local-user tinychen password cipher easy1234
Info: Add a new user.
[Huawei-aaa]local-user tinychen privilege level 3
[Huawei-aaa]local-user tinychen service-type ssh
[Huawei-aaa]quit
[Huawei]ssh user tinychen authentication-type password
 Authentication type setted, and will be in effect next time
[Huawei]q
<Huawei>save
  The current configuration will be written to the device. 
  Are you sure to continue? (y/n)[n]:y
  It will take several minutes to save configuration file, please wait.......
  Configuration file had been saved successfully
  Note: The configuration file will take effect after being activated
<Huawei>
```

## 华为S5700

### 配置IP地址

```
The device is running!

<Huawei>
<Huawei>sys
Enter system view, return user view with Ctrl+Z.
[Huawei]vlan 10
[Huawei-vlan10]q
[Huawei]int Vlanif 10
[Huawei-Vlanif10]ip address 192.168.126.4 24
[Huawei-Vlanif10]q
[Huawei]int GigabitEthernet 0/0/1
[Huawei-GigabitEthernet0/0/1]port link-type access
[Huawei-GigabitEthernet0/0/1]port default vlan 10
[Huawei-GigabitEthernet0/0/1]ping 192.168.126.1
  PING 192.168.126.1: 56  data bytes, press CTRL_C to break
    Reply from 192.168.126.1: bytes=56 Sequence=1 ttl=128 time=10 ms
    Reply from 192.168.126.1: bytes=56 Sequence=2 ttl=128 time=30 ms
    Reply from 192.168.126.1: bytes=56 Sequence=3 ttl=128 time=1 ms
    Reply from 192.168.126.1: bytes=56 Sequence=4 ttl=128 time=20 ms
    Reply from 192.168.126.1: bytes=56 Sequence=5 ttl=128 time=10 ms

  --- 192.168.126.1 ping statistics ---
    5 packet(s) transmitted
    5 packet(s) received
    0.00% packet loss
    round-trip min/avg/max = 1/14/30 ms

[Huawei-GigabitEthernet0/0/1]q
```



### 配置SSH服务

```
[Huawei]rsa local-key-pair create
The key name will be: Huawei_Host
The range of public key size is (512 ~ 2048). 
NOTES: If the key modulus is greater than 512, 
       it will take a few minutes.
Input the bits in the modulus[default = 512]:
Generating keys...
......++++++++++++
.++++++++++++
.....................++++++++
.............++++++++

[Huawei]stelnet server enable
Info: Succeeded in starting the Stelnet server.
[Huawei]user-interface vty 0 4
[Huawei-ui-vty0-4]authentication-mode aaa
[Huawei-ui-vty0-4]protocol inbound ssh
[Huawei-ui-vty0-4]q
[Huawei]aaa
[Huawei-aaa]local-user tinychen password cipher easy1234
Info: Add a new user.
[Huawei-aaa]local-user tinychen privilege level 3
[Huawei-aaa]local-user tinychen service-type ssh
[Huawei-aaa]quit
[Huawei]ssh user tinychen authentication-type password
Info: Succeeded in adding a new SSH user.
[Huawei]sysn	
[Huawei]sysname S5700
[S5700]q
<S5700>save
The current configuration will be written to the device.
Are you sure to continue?[Y/N]y
Info: Please input the file name ( *.cfg, *.zip ) [vrpcfg.zip]:
Now saving the current configuration to the slot 0.
Save the configuration successfully.
<S5700>
```

这个型号的交换机还需要额外配置下列命令，否则可能回出现无法ssh的情况。

```

<S5700>sys
Enter system view, return user view with Ctrl+Z.
[S5700]aaa
[S5700-aaa]local-user tinychen service-type ssh 	
[S5700-aaa]q
[S5700]ssh user tinychen service-type stelnet 
[S5700]display ssh user-information tinychen
       User Name            : tinychen
       Authentication-type  : password
       User-public-key-name : -
       User-public-key-type : -
       Sftp-directory       : -
       Service-type         : stelnet
       Authorization-cmd    : No
[S5700]q
<S5700>save
The current configuration will be written to the device.
Are you sure to continue?[Y/N]y
Now saving the current configuration to the slot 0.
Save the configuration successfully.
```

