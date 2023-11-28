import re


def testregex(regex, string):
    return re.match(regex, string) is not None


def encode(donné):
    if type(donné) == str: return donné.encode()
    if type(donné) == int:
        nbr_octet = 1
        while True:
            try:
                return donné.to_bytes(nbr_octet, 'big')
            except OverflowError:
                nbr_octet += 1
                continue

def decode(donné):
    types = {'str': 0, 'int': 1, 'float': 2, 'bool': 3}
    if donné[0] == types['str']: return donné[1:].decode()
    elif donné[0] == types['int']: return int.from_bytes(donné[1:], 'big')
    else : return int.from_bytes(donné, 'big')
