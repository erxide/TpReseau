import socket
from func import *

regex = r'^\d+\s[+\-*]\s\d+$'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('9.2.4.3', 13337))
s.send('Hello'.encode())

# On reçoit la string Hello
data = s.recv(1024)

# Récupération d'une string utilisateur

while True:
    msg = input("Calcul à envoyer: ")
    if not testregex(regex, msg): print("format invalide ou mauvais operateur( ex: 1 + 1 )"); continue
    msgtab = msg.split()
    if int(msgtab[0]) > 4294967295 or int(msgtab[2]) > 4294967295: print("Nombres trop grand"); continue
    else: break

header = len(msg).to_bytes(4, byteorder='big')


payload = header + encode(msg) + encode(0)


s.send(payload)

# Réception et affichage du résultat
s_data = s.recv(1024)
print(s_data.decode())
s.close()
