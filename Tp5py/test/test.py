

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
    return len(donné).to_bytes(1, 'big')

def decode(donné):
    types = {'str': 0, 'int': 1, 'float': 2, 'bool': 3}
    if donné[0] == types['str']: return donné[1:].decode()
    elif donné[0] == types['int']: return int.from_bytes(donné[1:], 'big')
    else : return int.from_bytes(donné, 'big')

if __name__ == '__main__':
    donné = 'Hello World'
    print(byte_len(encode(donné)))
    print(decode(byte_len(encode(donné))))
    print(encode(donné))
    print(decode(encode(donné)))
    




