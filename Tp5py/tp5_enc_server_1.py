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
            first_int_nbr_octet = header[1]
            operator_nbr_octet = header[2]
            second_int_nbr_octet = header[3]
            print(f"first_int_nbr_octet: {first_int_nbr_octet}\noperator_nbr_octet: {operator_nbr_octet}\nsecond_int_nbr_octet: {second_int_nbr_octet}")
            first_int_octet = conn.recv(first_int_nbr_octet)
            operator_octet = conn.recv(operator_nbr_octet)
            second_int_nbr_octet = conn.recv(second_int_nbr_octet)
            first_int = int.from_bytes(first_int_octet, byteorder='big')
            operator = operator_octet.decode()
            second_int = int.from_bytes(second_int_nbr_octet, byteorder='big')
            calc = f"{first_int} {operator} {second_int}"
            print(calc)
            end = conn.recv(1)
            if end != b'\x00': conn.send("error occured".encode()); break
            res = eval(calc)

            # Evaluation et envoi du résultat
            conn.send(encode(f"{calc} = {res}"))
            conn.close()
            break
            
        except socket.error:
            print("Error Occured.")
            conn.close()
            break

