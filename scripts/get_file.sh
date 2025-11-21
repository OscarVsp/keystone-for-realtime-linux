#!/usr/bin/expect -f

set timeout 60
set keystone_ip 192.168.1.213
set password sifive
set filename cyclictest.log

spawn scp -o StrictHostKeyChecking=no root@$keystone_ip:/root/$filename /home/oscar/Cyberlab/Sources/PhD/Codes/keystone-for-real-time-system/results/$filename
expect "password: "
send "$password\r"
expect eof