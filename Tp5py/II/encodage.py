
class Encodage:
    
    def encode(self, donné):
        if type(donné) == str: return donné.encode()
        if type(donné) == int:
            nbr_octet = 1
            while True:
                try:
                    return donné.to_bytes(nbr_octet, 'big')
                except OverflowError:
                    nbr_octet += 1
                    continue
    
    def decode_int(self, donné):
        return int.from_bytes(donné, 'big')
    
    def decode_str(self, donné):
        return donné.decode()