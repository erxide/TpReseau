import socket

host = "9.2.4.3"
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((host, port))
    print(f"Connecté avec succès au serveur {host} sur le port {port}")
    user_input = input("Que veux-tu envoyer au serveur : ")
    try:
        s.send(user_input.encode())
        data = s.recv(1024)
        print(f"Le serveur a répondu: {data.decode()}")
    except socket.error:
        print("Erreur lors de l'envoi.")
except socket.error:
    print("La connexion a échoué.")


s.close()