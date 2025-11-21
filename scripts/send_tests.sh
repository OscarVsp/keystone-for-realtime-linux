#!/usr/bin/expect -f

set timeout 60
set keystone_ip 192.168.1.213
set password sifive

spawn scp -o StrictHostKeyChecking=no -r /home/oscar/Cyberlab/Sources/PhD/Codes/keystone-for-real-time-system/keystone-6.6/overlays/keystone/fs/root root@$keystone_ip:/
expect "password: "
send "$password\r"
expect eof