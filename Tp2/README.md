## Topologie
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