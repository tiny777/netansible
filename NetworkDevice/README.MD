# 0 概述

这个脚本需要实现的功能很简单，就是自动ssh登录到网络设备上，查询相应的白名单，然后将结果导出成excel表格，具体的操作命令如下，对应的设备是华为的AC6605。

```
操作步骤

# 执行命令system-view，进入系统视图。
system-view

# 执行命令wlan，进入WLAN视图。
wlan

# 查看特定白名单内的信息
display sta-whitelist-profile name profilename

```

- 由于这里使用的是`netmiko`库，所以除了华为的网络设备，思科的设备也能支持，只需要在代码文件中稍作修改即可。

- 相应的命令也可以进行修改成其他的系列命令



# 1 软件版本

eNSP的BUG非常多，这里搭建拓扑来进行测试使用的软件版本是

- `eNSP 1.2.00.500 V100R002C00`
- `VirtualBox Graphical User Interface Version 5.1.26r117224(Qt5.6.2)`
- `WinPcap_4_1_3`
- Wireshark没有用到，版本应该无所谓
- 操作系统是`win10 pro`，`Microsoft Windows Version 1903(OS Build 18362.239)`



# 2 配置eNSP桥接真机

这里使用的是AC6605，对真机进行桥接，使用的桥接网卡是VMware WorkStation 15.1 的VMnet8网卡，即NAT模式的网卡，不是eNSP上面的192.168.56.1的那个网卡（这个老是有问题，各种ping不同）。



![mark](http://qiniuyun.tiny777.com/blog/20190816/cpwtbe7uUvBF.png)



接下来的eNSP内的桥接配置就十分简单了，添加一个UDP端口，然后添加一个网卡，再添加端口映射，就可以了。可以参考下面的这张图。

![mark](http://qiniuyun.tiny777.com/blog/20190816/TxJqKjGMH9CU.png)



接着我们拖入一个设备，我这里使用的是华为的AC6605。

给它配置一个IP地址然后测试一下。

```
[AC6605]vlan batch 10
Info: This operation may take a few seconds. Please wait for a moment...done.
[AC6605]int Vlanif 10
[AC6605-Vlanif10]ip address 192.168.59.2 24
[AC6605-Vlanif10]q
[AC6605]int GigabitEthernet 0/0/1
[AC6605-GigabitEthernet0/0/1]port link-type access 
[AC6605-GigabitEthernet0/0/1]port default vlan 10
```

![mark](http://qiniuyun.tiny777.com/blog/20190816/g43DkiCQiUkV.png)



然后我们ping一下真机的网卡，能通就说明桥接成功了。

![mark](http://qiniuyun.tiny777.com/blog/20190816/ySXeeAXjIs3a.png)





# 3 配置SSH服务



首先进行系统视图，然后创建`rsa key`，全部选择默认，接着启动`stelnet`服务。

```
system-view 
rsa local-key-pair create
stelnet server enable
```

接着配置用来远程的终端

```
system-view
user-interface vty 0 4
authentication-mode aaa
protocol inbound ssh
```

然后创建用户并设置密码。然后启动ssh服务。

```
system-view 
aaa
local-user tinychen password irreversible-cipher easy1234
local-user tinychen privilege level 3
local-user tinychen service-type ssh
quit
```

最后回到系统视图下，设置ssh用户的登录方式为密码登录。

```
ssh user tinychen authentication-type password
```



# 4 保存配置

**上面的所有配置如果不保存，当前的终端退出就会失效，所以要记得保存配置，方法是退到最开始的登录视图输入save就能保存了。**



# 5 `def sshLogin`

这里使用`netmiko`来对网络设备进行`ssh`登录，考虑到获取到的结果是包含了命令执行过程中的所有套接字，因此得到结果之后，先将其全部写入一个`debug.log`文件中保存记录，再将该次的操作结果写入`cache`文件用于下一步处理。

# 6 `def sort_to_csv`

对于输出的结果进行筛选处理，我们需要用到`re`库的正则表达式，以及`split()`，因为大多数的输出结果是以空格来分列的，因此使用`split()`来处理这些字符是最好不过的了。

最后导出成`csv`文件而不是直接导出excel的`xlsx`文件则是因为`csv`相比`xlsx`更容易读取处理，转成其他格式也更加方便。

# 7  `def csv_to_xlsx_pd`

这里就是使用`pandas`库来将上一步生成的`csv`转为`xlsx`文件了，非常的简单，需要的注意的就是添加的行名和列名参数。