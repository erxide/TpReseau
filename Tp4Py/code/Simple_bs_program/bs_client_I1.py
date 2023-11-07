import socket

host = ""
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

s.send(b"Meooooo !")

data = s.recv(1024)

s.close()

print(f"Le serveur a répondu: {repr(data)}")