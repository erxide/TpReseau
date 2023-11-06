import os

def ping():
    system = os.name
    if system == 'nt':
        commande = 'ping -n 4 8.8.8.8'
    elif system == 'posix':
        commande = 'ping -c 4 8.8.8.8'
    os.system(commande)

ping()
