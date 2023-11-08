import socket
import logging

host = "9.2.4.3"
port = 13337

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%y-%m-%d %H:%M:%S')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
logging.info(f"Le serveur tourne {host}:{port}.")

s.listen(1)

conn , addr = s.accept()
logging.info(f'Un client {addr} vient de se co.')

while True:
    
    try:
        data = conn.recv(1024)
        if not data: break
        if "meo" in data.decode() : conn.send("Meo à toi confrère.".encode())
        elif "waf" in data.decode() : conn.send("ptdr t ki".encode())
        elif not "waf" in data.decode() or not "meo" in data.decode : conn.send("Mes respects humble humain.".encode())

    except socket.error:
        print("Error Occured.")
        break

conn.close()