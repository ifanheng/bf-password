#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "使用说明: $0 username"
    echo "   username: 指定扫描那个用户的密码"
    exit 1
fi

username=$1
hosts_file="./hosts"

scan_log="./scan.log"

> $scan_log

for host in `cat $hosts_file`
do
    python bf-password.py $host $username >> $scan_log &
done
