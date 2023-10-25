# I :Topologie
### Compte-rendu

```bash 
    [esinck@node1 ~]$ ip a
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
    2: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:50:97:a5 brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.11/24 brd 10.1.1.255 scope global noprefixroute enp0s8
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fe50:97a5/64 scope link
       valid_lft forever preferred_lft forever
    [esinck@node1 ~]$ ip r s
    10.1.1.0/24 dev enp0s8 proto kernel scope link src 10.1.1.11 metric 100
    10.1.2.0/24 via 10.1.1.254 dev enp0s8 proto static metric 100
    [esinck@node1 ~]$ ping 10.1.2.12
    PING 10.1.2.12 (10.1.2.12) 56(84) bytes of data.
    64 bytes from 10.1.2.12: icmp_seq=1 ttl=63 time=1.14 ms
    64 bytes from 10.1.2.12: icmp_seq=2 ttl=63 time=1.40 ms
    64 bytes from 10.1.2.12: icmp_seq=3 ttl=63 time=1.36 ms
    64 bytes from 10.1.2.12: icmp_seq=4 ttl=63 time=1.33 ms
    ^C
    --- 10.1.2.12 ping statistics ---
    4 packets transmitted, 4 received, 0% packet loss, time 3007ms
    rtt min/avg/max/mdev = 1.139/1.307/1.399/0.100 ms
    [esinck@node1 ~]$ traceroute 10.1.2.0
    traceroute to 10.1.2.0 (10.1.2.0), 30 hops max, 60 byte packets
    1  10.1.1.254 (10.1.1.254)  1.114 ms  1.092 ms  1.020 ms
    2  10.1.2.254 (10.1.2.254)  3142.663 ms !H  3142.635 ms !H  3142.452 ms !H
```
![aaaaaaa](/img/83rub8.jpg)

# II. Interlude accès internet
☀️ **Sur `router.tp2`**
```bash
[esinck@routeur ~]$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=56 time=14.1 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=56 time=12.6 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=56 time=14.6 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=56 time=14.6 ms
^C
--- 8.8.8.8 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3008ms
rtt min/avg/max/mdev = 12.604/13.995/14.649/0.825 ms
[esinck@routeur ~]$ ping google.com
PING google.com (216.58.214.174) 56(84) bytes of data.
64 bytes from par10s42-in-f14.1e100.net (216.58.214.174): icmp_seq=1 ttl=56 time=21.9 ms
64 bytes from par10s42-in-f14.1e100.net (216.58.214.174): icmp_seq=2 ttl=56 time=23.9 ms
64 bytes from mad01s26-in-f174.1e100.net (216.58.214.174): icmp_seq=3 ttl=56 time=25.6 ms
64 bytes from mad01s26-in-f14.1e100.net (216.58.214.174): icmp_seq=4 ttl=56 time=23.9 ms
^C
--- google.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3006ms
rtt min/avg/max/mdev = 21.856/23.825/25.619/1.333 ms
```

☀️ **Accès internet `LAN1` et `LAN2`**`
```bash
[esinck@node2 ~]$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=113 time=16.2 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=113 time=16.4 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=113 time=16.3 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=113 time=16.6 ms
^C
--- 8.8.8.8 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3089ms
rtt min/avg/max/mdev = 16.225/16.373/16.619/0.152 ms
[esinck@node2 ~]$ ping google.com
PING google.com (216.58.214.174) 56(84) bytes of data.
64 bytes from mad01s26-in-f14.1e100.net (216.58.214.174): icmp_seq=1 ttl=114 time=16.3 ms
64 bytes from par10s42-in-f14.1e100.net (216.58.214.174): icmp_seq=2 ttl=114 time=22.1 ms
64 bytes from mad01s26-in-f174.1e100.net (216.58.214.174): icmp_seq=3 ttl=114 time=16.9 ms
64 bytes from par10s42-in-f14.1e100.net (216.58.214.174): icmp_seq=4 ttl=114 time=17.0 ms
^C
--- google.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3088ms
rtt min/avg/max/mdev = 16.299/18.061/22.106/2.349 ms
```
![tentation](/img/83rs65.png)
# III. Services réseau

## 1. DHCP

☀️ **Sur `dhcp.lan1.tp2`**
```bash 
[esinck@dhcp ~]$ sudo dnf -y install dhcp-server
[esinck@dhcp ~]$ sudo cat /etc/dhcp/dhcpd.conf
[sudo] password for esinck:
#
# DHCP Server Configuration file.
#   see /usr/share/doc/dhcp-server/dhcpd.conf.example
#   see dhcpd.conf(5) man page
#
# create new
# specify domain name
option domain-name     "srv.world";

# specify DNS server's hostname or IP address
option domain-name-servers     dlp.srv.world;

# default lease time
default-lease-time 600;

# max lease time
max-lease-time 7200;

# this DHCP server to be declared valid
authoritative;

# specify network address and subnetmask
subnet 10.1.1.0 netmask 255.255.255.0 {
    # specify the range of lease IP addresses
    range 10.1.1.100 10.1.1.200;

    # specify gateway (router)
    option routers 10.1.1.254;  # Gateway IP address

    # specify DNS server
    option domain-name-servers 1.1.1.1;  # DNS server IP address
    option broadcast-address 10.1.1.255;
}
[esinck@dhcp ~]$ sudo systemctl enable --now dhcpd
[esinck@dhcp ~]$ sudo firewall-cmd --add-service=dhcp
success
[esinck@dhcp ~]$ sudo firewall-cmd --runtime-to-permanent
success
[esinck@dhcp ~]$ systemctl is-active dhcpd
active
```
☀️ **Sur `node1.lan1.tp2`**
```bash
[esinck@node1 ~]$ cat /etc/sysconfig/network-scripts/ifcfg-enp0s8
NAME=enp0s8
DEVICE=enp0s8

BOOTPROTO=dhcp
ONBOOT=yes

[esinck@node1 ~]$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:50:97:a5 brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.100/24 brd 10.1.1.255 scope global dynamic noprefixroute enp0s8
       valid_lft 482sec preferred_lft 482sec
    inet6 fe80::a00:27ff:fe50:97a5/64 scope link
       valid_lft forever preferred_lft forever
[esinck@node1 ~]$ ping google.com
PING google.com (172.217.20.206) 56(84) bytes of data.
64 bytes from par10s50-in-f14.1e100.net (172.217.20.206): icmp_seq=1 ttl=115 time=15.9 ms
64 bytes from waw02s08-in-f14.1e100.net (172.217.20.206): icmp_seq=2 ttl=115 time=16.4 ms
^C
--- google.com ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1014ms
rtt min/avg/max/mdev = 15.885/16.166/16.448/0.281 ms
[esinck@node1 ~]$ ping 10.1.2.11
PING 10.1.2.11 (10.1.2.11) 56(84) bytes of data.
64 bytes from 10.1.2.11: icmp_seq=1 ttl=63 time=0.800 ms
64 bytes from 10.1.2.11: icmp_seq=2 ttl=63 time=1.51 ms
^C
--- 10.1.2.11 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1061ms
rtt min/avg/max/mdev = 0.800/1.157/1.514/0.357 ms
```

## 2. Web web web



☀️ **Sur `web.lan2.tp2`**
```bash
sudo dnf install nginx
sudo systemctl start nginx
sudo systemctl enable nginx
sudo mkdir /var/www/
sudo mkdir /var/www/site_nul/
sudo nano /etc/nginx/conf.d/site_nul.conf
server {
    listen 80;
    server_name site_nul.tp2;

    root /var/www/site_nul;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}
sudo systemctl restart nginx
sudo systemctl status nginx
● nginx.service - The nginx HTTP and reverse proxy server
     Loaded: loaded (/usr/lib/systemd/system/nginx.service; enabled; preset: disabled)
     Active: active (running) since Wed 2023-10-25 14:10:48 CEST; 32s ago
   Main PID: 1309 (nginx)
      Tasks: 3 (limit: 23110)
     Memory: 4.2M
        CPU: 27ms
     CGroup: /system.slice/nginx.service
             ├─1309 "nginx: master process /usr/sbin/nginx"
             ├─1310 "nginx: worker process"
             └─1311 "nginx: worker process"

Oct 25 14:10:48 web.lan2.tp2 systemd[1]: Starting The nginx HTTP and reverse proxy server...
Oct 25 14:10:48 web.lan2.tp2 nginx[1307]: nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
Oct 25 14:10:48 web.lan2.tp2 nginx[1307]: nginx: configuration file /etc/nginx/nginx.conf test is successful
Oct 25 14:10:48 web.lan2.tp2 systemd[1]: Started The nginx HTTP and reverse proxy server.
sudo firewall-cmd --zone=public --add-service=http --permanent
success
sudo firewall-cmd --zone=public --add-service=https --permanent
success
sudo firewall-cmd --reload
success
sudo ss -altp | grep nginx
LISTEN 0      511          0.0.0.0:http      0.0.0.0:*    users:(("nginx",pid=820,fd=6),("nginx",pid=819,fd=6),("nginx",pid=818,fd=6))
LISTEN 0      511             [::]:http         [::]:*    users:(("nginx",pid=820,fd=7),("nginx",pid=819,fd=7),("nginx",pid=818,fd=7))

```

☀️ **Sur `node1.lan1.tp2`**
```bash
curl site_nul.tp2
<!DOCTYPE html>
<html>
<head>
    <title>My Nul Site</title>
</head>
<body>
    <h1>Welcome to my Nul site!</h1>
    <p>This is a test page.</p>
</body>
</html>
```


![tpfiniciao](/img/83rszy.gif)
