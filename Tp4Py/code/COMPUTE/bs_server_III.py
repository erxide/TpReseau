import socket
import logging
import os
import time
import threading

host = "9.2.4.3"
port = 13337


if not os.path.exists('/var/log/bs_server'):
    os.makedirs('/var/log/bs_server')


logging.basicConfig(filename='/var/log/bs_server/bs_server.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

logging.info(f"Démarage du serveur.")
print("\033[255m" + "INFO" + "\033[0m", f"Démarage du serveur.")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
logging.info(f"Le serveur tourne {host}:{port}.")
print("\033[255m" + "INFO" + "\033[0m", f"Le serveur tourne sur {host}:{port}")

last_connection_time = time.time()

def check_connections():
    global last_connection_time
    while True:
        time.sleep(60)
        if time.time() - last_connection_time > 60:
            logging.warning("Aucun client depuis plus de une minute.")
            print("\033[93m" + "WARN" + "\033[0m", "Aucun client depuis plus de une minute.")

# Démarrer le thread de vérification des connexions
threading.Thread(target=check_connections, daemon=True).start()

s.listen(1)


while True:
    
    conn , addr = s.accept()
    last_connection_time = time.time() 
    logging.info(f'Un client {addr} vient de se co.')
    print("\033[255m" + "INFO" + "\033[0m", f"Un client {addr} vient de se co.")

    try:
        data = conn.recv(1024)
        if not data: break
        logging.info(f"Le client {addr} a envoyé: {data.decode()}")
        print("\033[255m" + "INFO" + "\033[0m", f"Le client {addr} a envoyé: {data.decode()}")
        try :
            message = eval(data.decode())
        except ZeroDivisionError:
            message = "Division par zero impossible"
        conn.send(message.encode())
        logging.info(f"Réponse envoyée au client {addr} : {message}")
        print("\033[255m" + "INFO" + "\033[0m", f"Réponse envoyée au client {addr} : {message}")
        break

    except socket.error:
        print("Error Occured.")
        break


logging.info(f"Fermeture du serveur.")
print("\033[255m" + "INFO" + "\033[0m", f"Fermeture du serveur.")
conn.close()