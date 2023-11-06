import lookup
import is_up
import get_ip
from sys import argv


commande = argv[1]
    

if commande == "lookup": lookup.lookup(argv[2])
elif commande == "ping": is_up.is_up(argv[2])
elif commande == "ip": get_ip.get_ip()
else:print(f"{commande} is not an available command. Déso")


