import os
from sys import argv

def is_up(ip : str = '8.8.8.8'):
    # if len(argv) < 2:
    #     print('Veuillez entrez une adresse IP')
    #     exit()
    #else :
        # ip = argv[1]
        system = os.name
        if system == 'nt':
            commande = f'ping -n 1 {ip} > nul 2>&1'
        elif system == 'posix':
            commande = f'ping -c 1 {ip} > /dev/null 2>&1'
        resultat = os.system(commande)
        if resultat == 0 :
            print('UP !')
        else :  
            print('DOWN !')

