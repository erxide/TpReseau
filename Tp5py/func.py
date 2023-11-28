import re


def testregex(regex, string):
    return re.match(regex, string) is not None

def len_in_byte(string):
    return len(string).to_bytes(1, byteorder="big")

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
