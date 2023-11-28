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

            # On reçoit le calcul du client
            header = conn.recv(4)
            first_int_nbr_octet = int.from_bytes(header[2], byteorder='big')
            operator_nbr_octet = int.from_bytes(header[3], byteorder='big')
            second_int_nbr_octet = int.from_bytes(header[4], byteorder='big')
            print(f"first_int_nbr_octet: {first_int_nbr_octet}\noperator_nbr_octet: {operator_nbr_octet}\nsecond_int_nbr_octet: {second_int_nbr_octet}")
            first_int = decode(int(conn.recv(first_int_nbr_octet)))
            operator = decode(str(conn.recv(operator_nbr_octet)))
            second_int = decode(int(conn.recv(second_int_nbr_octet)))
            calc = f"{first_int} {operator} {second_int}"
            print(calc)
            end = conn.recv(1)
            if end != b'\x00': conn.send("error occured".encode()); break
            res = eval(calc)

            # Evaluation et envoi du résultat
            conn.send(encode(f"{calc} = {res}"))
            
        except socket.error:
            print("Error Occured.")
            break

conn.close()
