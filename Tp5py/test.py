

def encode(donné):
    types = {'str': 0, 'int': 1, 'float': 2, 'bool': 3}
    if type(donné) == str: return int(types['str']).to_bytes(1, 'big') + donné.encode()
    if type(donné)== int :
        nbr_octet = 1
        while True :
            try : return int(types['int']).to_bytes(1, 'big') + donné.to_bytes(nbr_octet, 'big')
            except OverflowError:
                nbr_octet += 1
                continue

def byte_len(donné):
    return len(encode(donné)).to_bytes(1, 'big')

def decode(donné):
    types = {'str': 0, 'int': 1, 'float': 2, 'bool': 3}
    if donné[0] == types['str']: return donné[1:].decode()
    if donné[0] == types['int']: return int.from_bytes(donné[1:], 'big')
    else : return int.from_bytes(donné, 'big')

if __name__ == '__main__':
    donné = 894651984654654987654987654976594965499654
    m = encode(donné)
    print(m)
    print(decode(m))
    print(byte_len(donné))



