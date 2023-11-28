import socket

host = "localhost"
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))

s.listen(5)

conn, addr = s.accept()
print(f"Connexion de {addr}.")

data = conn.recv(1024)

print(data)

s.close