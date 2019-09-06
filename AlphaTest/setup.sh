#! /bin/bash

# 首先我们需要安装epel库
yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm -y

# 安装python3.6
yum install python36 -y

# 安装pip
yum install python36-pip -y

# 升级pip
pip3 install --upgrade pip

# 使用pip安装需要的库
pip install netmiko
pip install pandas
