import socket
import re 

host = "9.2.4.3"
port = 13337
patern = r"(waf|meo)"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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