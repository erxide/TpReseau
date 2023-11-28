import socket
from test import encode, decode, byte_len

host = "9.2.4.3"
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))

try :
    s.listen(1)

    conn, addr = s.accept()
    print(f"Connexion de {addr}.")
    len_msg = conn.recv(1)
    msg = conn.recv(int.from_bytes(decode(len_msg), 'big'))
    print(decode(msg))
except socket.error:
    print(socket.error)
    exit(1)
s.close