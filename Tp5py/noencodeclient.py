import socket 

host = "9.3.4.3"
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

s.send(1000)

s.close
