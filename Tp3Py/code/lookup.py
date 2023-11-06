import socket
from sys import argv

def lookup(nom_de_dommaine : str = 'google.com'):
    # if len(argv) < 2:
    #     print('Veuillez entrez un nom de domaine')
    #     exit()
    # nom_de_dommaine = argv[1]
    try :
        addresse_ip = socket.gethostbyname(nom_de_dommaine)
        print(addresse_ip)
    except socket.gaierror:
        print('Erreur de résolution de nom de domaine')
