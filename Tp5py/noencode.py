import socket

host = "localhost"
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.connect((host, port))

s.listen(5)

conn, addr = s.accept()

data = conn.recv(1)

print(data)

s.close