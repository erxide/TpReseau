import socket 
from test import encode, decode, byte_len

host = "9.2.4.3"
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((host, port))
    msg = encode("Hello World")
    len_msg = byte_len(msg)
    s.send(len_msg)
    s.send(msg)
except socket.error as r:
    print(r)
    exit(1)


s.close
