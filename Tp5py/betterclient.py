import socket
from encodage import Encodage
from func import testregex

class Calculatrice_Client(Encodage):

    def __init__(self):
        self.regex = r'^\d+\s[+\-\/*]\s\d+$'
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.content : str = ''
        self.contenttab : list = []

    def connect(self, host, port):
        
        self.s.connect((host, port))
        print(self.s.recv(1024).decode())

    def send(self, msg):
        self.s.send(msg)

    def recv(self, size) -> bytes:
        return self.s.recv(size)
    
    def close(self):
        self.s.close()

    def ask_calcul(self):
        while True:
            self.content = input("Calcul à envoyer: ")
            if self.content == "stop": self.close(); exit(0)
            if not testregex(self.regex, self.content): print("format invalide ou mauvais operateur( ex: 1 + 1 )"); continue
            self.contenttab = self.content.split()
            if int(self.contenttab[0]) > 4294967295 or int(self.contenttab[2]) > 4294967295: print("Nombres trop grand"); continue
            else: break
    
    def create_header(self):
        return self.encode(len(self.encode(self.content))) + self.encode(len(self.encode(int(self.contenttab[0])))) + self.encode(len(self.encode(str(self.contenttab[1])))) + self.encode(len(self.encode(int(self.contenttab[2]))))

    def create_msg(self):
        return self.encode(int(self.contenttab[0])) + self.encode(str(self.contenttab[1])) + self.encode(int(self.contenttab[2]))

    def create_payload(self):
        return self.create_header() + self.create_msg() + self.encode(0)
    


if __name__ == "__main__":
    client = Calculatrice_Client()
    client.connect('9.2.4.3', 13337)
    while True:
        client.ask_calcul()
        client.send(client.create_payload())
        print(client.recv(1024).decode())
        client.close()
        break


