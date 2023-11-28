import socket
from func import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('9.2.4.3', 13337))  

while True:
    s.listen(1)
    conn, addr = s.accept()

    while True:

        try:
            # On reçoit la string Hello du client
            data = conn.recv(1024)
            if not data: break

            conn.send("Hello".encode())

            # On reçoit le calcul du client
            len_next_msg = conn.recv(4)
            next_msg = conn.recv(int.from_bytes(len_next_msg, byteorder='big'))
            end = conn.recv(1)
            if end != b'\x00': conn.send("error occured".encode()); break
            res = eval(next_msg.decode())

            # Evaluation et envoi du résultat
            conn.send(encode(f"{next_msg.decode()} = {res}"))
            
        except socket.error:
            print("Error Occured.")
            break

conn.close()
