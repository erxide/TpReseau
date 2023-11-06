import psutil
import socket

def get_ip():
    for interface, addresses in psutil.net_if_addrs().items():
        for addresse in addresses:
            if addresse.family == socket.AF_INET:
                print(f"{interface} : {addresse.address}")