import socket

class Calculatrice_Client():

    def __init__(self):
        pass

    def connect(self, host, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host, port))
        print(self.s.recv(1024).decode())

    def send(self, msg):
        self.s.send(msg)
