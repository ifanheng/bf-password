
通过一个密码字典，来扫描指定ssh用户的账号密码，支持单台扫描和多台同时扫描

执行环境：python3

# 安装依赖
pip3 install gevent

pip3 install paramiko

# 密码文件
./passwd

# 主机文件
./hosts

# 使用方法
每次只能扫描一个用户

## 1. 只扫描一台主机

```
# python3 bf-password.py 192.168.10.16 root

192.168.16.16 root 123456
```
```
# python3 bf-password.py 192.168.10.16 username

192.168.16.16 username abc,123
```

## 2. 扫描多台主机
把ip或者主机名逐行写入到 hosts 文件中

```
bash scan-hosts.sh username
```
密码信息会输出到scan.log文件中，这个文件每次执行都会先清空内容
