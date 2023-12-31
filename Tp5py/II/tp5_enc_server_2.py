import socket
from encodage import Encodage 

class Calculatrice_Server(Encodage):
    
    def __init__(self):
        self.resultat : int = 0
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.nbr_octet_total : int = 0
        self.first_int_nbr_octet : int = 0
        self.operator_nbr_octet : int = 0
        self.second_int_nbr_octet : int = 0
        self.first_int_octet : bytes = b''
        self.operator_octet : bytes = b''
        self.second_int_octet : bytes = b''
        self.first_int : int = 0
        self.operator : str = ''
        self.second_int : int = 0
        self.calc : str = ''
        self.connisup : bool = False

        

    def bind(self, host, port):
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((host, port))

    def is_connected(self) -> bool:
        return self.s.fileno() != -1
    
    
    def listen(self):
        a = 0
        self.s.settimeout(5.0)
        while True :
            try :
                self.s.listen(1)
                self.conn, self.addr = self.s.accept()
                print(f"Connexion de {self.addr}.")
                self.connisup = True
                self.s.settimeout(None)
                break
            except socket.timeout:
                a += 1
                if a == 12 : print("[WARM] Aucun client depuis plus une minute."); a = 0; 
    def send(self, msg):
        if type(msg) == str: self.conn.send(self.encode(msg))
        elif type(msg) == bytes: self.conn.send(msg)
        elif type(msg) == int: self.conn.send(self.encode(msg))
        else: self.conn.send(msg)

    def recv(self, size) -> bytes:
        return self.conn.recv(size)
    
    def close_conn(self):
        print(f"Connexion de {self.addr} fermée.")
        self.connisup = False
        self.conn.close()
    
    def close_s(self):
        print("Serveur fermé.")
        self.s.close()

    def calcul(self, calcul):
        try:    
            return eval(calcul)
        except ZeroDivisionError:
            return "Division par zero impossible"
        except SyntaxError:
            return "Erreur de syntaxe"
        except NameError:
            return "Erreur de syntaxe"
        except TypeError:
            self.close_conn()
            return "Erreur de syntaxe"
        except OverflowError:
            return "Erreur de syntaxe"
    
    def traitement_header(self):
        try :
            header = self.recv(4)
            self.nbr_octet_total = header[0]
            self.first_int_nbr_octet = header[1]
            self.operator_nbr_octet = header[2]
            self.second_int_nbr_octet = header[3]
            return self.nbr_octet_total, self.first_int_nbr_octet, self.operator_nbr_octet, self.second_int_nbr_octet
        except IndexError:
            print("Erreur occured")
    
    def traitement_calcul(self):
        self.first_int_octet = self.recv(self.first_int_nbr_octet)
        self.operator_octet = self.recv(self.operator_nbr_octet)
        self.second_int_octet = self.recv(self.second_int_nbr_octet)
        self.first_int = self.decode_int(self.first_int_octet)
        self.operator = self.decode_str(self.operator_octet)
        self.second_int = self.decode_int(self.second_int_octet)
        self.calc = f"{self.first_int} {self.operator} {self.second_int}"
        return self.first_int, self.operator, self.second_int, self.calc
    
    def traitement_end(self):
        end = self.recv(1)
        if end != b'\x00': self.send(self.encode("Erreur occured")); return True
        return False
            
    
    def traitement(self):
        self.traitement_header()
        self.traitement_calcul()
        if self.traitement_end(): print("Erreur occured")
        else : return self.calc
    

if __name__ == "__main__":
    srv = Calculatrice_Server()
    srv.bind('9.2.4.3', 13337)
    while srv.is_connected():
        srv.listen()
        srv.send("Bienvenue sur la calculatrice !\n".encode())
        try:
            calc = srv.traitement()
            res = srv.calcul(calc)
            srv.send(f"{calc} = {res}")
            srv.close_conn()
            continue
        except socket.error as e:
            print("Error Occured: ", e)
            srv.send("Error Occured : ", e)
            continue
srv.close_s()

