import socket
import re 
from sys import argv
import logging
import os

host = "9.2.4.3"
port = 13337
patern = r"[+\-*/]"

if not os.path.exists('log/bs_client'):
    os.makedirs('log/bs_client')


logging.basicConfig(filename='log/bs_client/bs_client.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

if len(argv) >= 2:
    option = argv[1]
    if option == "-p" or option == "--port":
        port = int(argv[2])
        if port < 0 or port > 65535:
            print("\033[91m" + "ERROR Le port spécifié n'est pas un port possible (de 0 à 65535)" + "\033[0m")
            exit(1)
        elif port >= 0 and port <= 1024 :
            print("\033[91m" + "ERROR Le port spécifié est un port privilégié. Spécifiez un port au dessus de 1024" + "\033[0m")
            exit(2)
    elif option == "-h" or option == "--help":
        print("Usage: python3 bs_server_II1.py [OPTION]")
        print("Options:")
        print("  -h, --help\t\t\tAffiche l'aide")
        print("  -p, --port\t\t\tPort sur lequel le serveur va se connecter bs_server_II1.py -p [PORT] or bs_server_II1.py --port [PORT]")
        exit(0)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((host, port))
    logging.info(f"Connexion réussie à {host}:{port}.")
    print(f"Connexion réussie à {host}:{port}.")
    user_input = input("Que veux-tu envoyer au serveur : ")
    if type(user_input) != str:
        print("\033[91m" + f"ERROR Le message envoyé au serveur doit etre une string"+ "\033[0m")
        logging.error("La donnée envoyé n'est pas une string") #raise TypeError("La donnée envoyée au serveur doit être de type str")
        exit(1)
    if re.search(patern, user_input) == None:
        print("\033[91m" + f"ERROR Le message envoyé au serveur doit contenir un opérateur comme \"+\", \"-\", \"*\" ou \"/\"."+ "\033[0m") #raise ValueError("La donnée envoyée au serveur doit contenir le mot 'meo' ou 'waf'")
        logging.error(f"Le message envoyé au serveur ne contient pas de calcul.")
        exit(1)
    try:
        s.send(user_input.encode())
        logging.info(f"Message envoyé au serveur {host} : {user_input}")
        data = s.recv(1024)
        print(f"Le serveur a répondu: {data.decode()}")
        logging.info(f"Réponse reçue du serveur {host} : {data.decode()}")
    except socket.error:
        print("Erreur lors de l'envoi.")
except socket.error:
    logging.error(f"Impossible de se connecter au serveur {host} sur le {port}.")
    print("\033[91m" + f"ERROR Impossible de se connecter au serveur {host} sur le {port}."+ "\033[0m")


s.close()