import socket
import re 
from sys import argv

host = "9.2.4.3"
port = 13337
patern = r"(waf|meo)"
option = argv[1]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(argv) == 3:
    if option == "-p" or option == "--port":
        port = int(argv[2])
        if port < 0 or port > 65535:
            print("ERROR Le port spécifié n'est pas un port possible (de 0 à 65535)")
            exit(1)
        elif port >= 0 and port <= 1024 :
            print("ERROR Le port spécifié est un port privilégié. Spécifiez un port au dessus de 1024")
            exit(2)
    if option == "-h" or option == "--help":
        pass


try:
    s.connect((host, port))
    print(f"Connecté avec succès au serveur {host} sur le port {port}")
    user_input = input("Que veux-tu envoyer au serveur : ")
    if type(user_input) != str:
        raise TypeError("La donnée envoyée au serveur doit être de type str") 
    if re.search(patern, user_input) == None:
        raise ValueError("La donnée envoyée au serveur doit contenir le mot 'meo' ou 'waf'")
    try:
        s.send(user_input.encode())
        data = s.recv(1024)
        print(f"Le serveur a répondu: {data.decode()}")
    except socket.error:
        print("Erreur lors de l'envoi.")
except socket.error:
    print("La connexion a échoué.")


s.close()