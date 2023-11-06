import os
from sys import argv

def ping_arg():
    if len(argv) < 2:
        print('Veuillez entrez une adresse IP')
        exit()
    else :
        ip = argv[1]
        system = os.name
        if system == 'nt':
            commande = f'ping -n 4 {ip}'
        elif system == 'posix':
            commande = f'ping -c 4 {ip}'
        os.system(commande)

ping_arg()