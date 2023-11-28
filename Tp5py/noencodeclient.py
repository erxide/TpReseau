import socket 

host = "9.2.4.3"
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((host, port))
except socket.error:
    print("Impossible de se connecter au serveur.")
    exit(1)

s.send(1000)

s.close
