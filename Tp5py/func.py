import re
from encodage import Encodage as Enc


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
    if type(donné) == str: return donné.decode()
    elif type(donné) == int : return int.from_bytes(donné, 'big')
    else : return int.from_bytes(donné, 'big')


    