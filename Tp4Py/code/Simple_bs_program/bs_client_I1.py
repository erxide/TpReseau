import socket

host = "9.2.4.3"
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

s.send("Meooooo !".encode())

data = s.recv(1024)

s.close()

print(f"Le serveur a répondu: {repr(data)}")