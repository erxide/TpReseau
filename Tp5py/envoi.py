from __future__ import print_function

class Envoi:
    

    def recv(self, size) -> bytes:
        return self.s.recv(size)
    
    
    def send(self, msg):
        if type(msg) == str: self.conn.send(self.encode(msg))
        elif type(msg) == bytes: self.conn.send(msg)
        elif type(msg) == int: self.conn.send(self.encode(msg))
        else: self.conn.send(msg)