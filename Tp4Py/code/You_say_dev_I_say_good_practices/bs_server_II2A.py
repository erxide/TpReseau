import socket
import logging
import os

host = "9.2.4.3"
port = 13337


if not os.path.exists('/var/log/bs_server'):
    os.makedirs('/var/log/bs_server')


logging.basicConfig(filename='/var/log/bs_server/bs_server.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
logging.info(f"Le serveur tourne {host}:{port}.")
print("\033[255m" + "INFO" + "\033[0m", f"Le serveur tourne sur {host}:{port}")

s.listen(1)



conn , addr = s.accept()
logging.info(f'Un client {addr} vient de se co.')
print("\033[255m" + "INFO" + "\033[0m", f"Un client {addr} vient de se co.")

while True:
    
    try:
        data = conn.recv(1024)
        if not data: break
        logging.info(f"Le client {addr} a envoyé: {data.decode()}")
        print("\033[255m" + "INFO" + "\033[0m", f"Le client {addr} a envoyé: {data.decode()}")
        if "meo" in data.decode() : message = "Meo à toi confrère." #conn.send("Meo à toi confrère.".encode())
        elif "waf" in data.decode() : message = "ptdr t ki" #conn.send("ptdr t ki".encode())
        elif not "waf" in data.decode() or not "meo" in data.decode : message = "Mes repects humble humain." #conn.send("Mes respects humble humain.".encode())
        conn.send(message.encode())
        logging.info(f"Réponse envoyée au client {addr} : {message}")
        print("\033[255m" + "INFO" + "\033[0m", f"Réponse envoyée au client {addr} : {message}")

    except socket.error:
        print("Error Occured.")
        break

conn.close()