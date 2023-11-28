import socket

host = "127.0.0.1"
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))

try :
    s.listen(1)

    conn, addr = s.accept()
    print(f"Connexion de {addr}.")

    data = conn.recv(1024)

    print(data)
except socket.error:
    print(socket.error)
    exit(1)
s.close