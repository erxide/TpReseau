# TP1 : Maîtrise réseau du poste

Pour ce TP, on va utiliser **uniquement votre poste** (pas de VM, rien, quedal, quetchi).

Le but du TP : se remettre dans le bain tranquillement en manipulant pas mal de concepts qu'on a vu l'an dernier.

C'est un premier TP *chill*, qui vous(ré)apprend à maîtriser votre poste en ce qui concerne le réseau. Faites le seul ou avec votre mate préféré bien sûr, mais jouez le jeu, faites vos propres recherches.

La "difficulté" va crescendo au fil du TP, mais la solution tombe très vite avec une ptite recherche Google si vos connaissances de l'an dernier deviennent floues.

- [TP1 : Maîtrise réseau du poste](#tp1--maîtrise-réseau-du-poste)
- [I. Basics](#i-basics)
- [II. Go further](#ii-go-further)
- [III. Le requin](#iii-le-requin)

# I. Basics

> Tout est à faire en ligne de commande, sauf si précision contraire.

☀️ **Carte réseau WiFi**

Déterminer...

- l'adresse MAC de votre carte WiFi : `BC-6E-E2-D3-54-28`
- l'adresse IP de votre carte WiFi : `10.33.76.224`
- le masque de sous-réseau du réseau LAN auquel vous êtes connectés en WiFi
  - en notation CIDR `/20`
  - ET en notation décimale `255.255.240.0`

---

☀️ **Déso pas déso**

Pas besoin d'un terminal là, juste une feuille, ou votre tête, ou un tool qui calcule tout hihi. Déterminer...

- l'adresse de réseau du LAN auquel vous êtes connectés en WiFi : `10.33.64.0`
- l'adresse de broadcast : `10.33.79.255`
- le nombre d'adresses IP disponibles dans ce réseau : `4094`

---

☀️ **Hostname**

- déterminer le hostname de votre PC : `erwanslave`

---

☀️ **Passerelle du réseau**

Déterminer...

- l'adresse IP de la passerelle du réseau : `10.33.79.254`
- l'adresse MAC de la passerelle du réseau : `7c-5a-1c-d3-d8-76`

---

☀️ **Serveur DHCP et DNS**

Déterminer...

- l'adresse IP du serveur DHCP qui vous a filé une IP : `10.33.79.254`
- l'adresse IP du serveur DNS que vous utilisez quand vous allez sur internet : `8.8.8.8 et 1.1.1.1`

---

☀️ **Table de routage**

Déterminer...

- dans votre table de routage, laquelle est la route par défaut : 

``` Itinéraires actifs :
    Destination réseau    Masque réseau  Adr. passerelle   Adr. interface   Métrique
     10.33.64.0          255.255.240.0      On-link          10.33.76.224     311
```

---


# II. Go further

> Toujours tout en ligne de commande.

---

☀️ **Hosts ?**

- faites en sorte que pour votre PC, le nom `b2.hello.vous` corresponde à l'IP `1.1.1.1`
- prouvez avec un `ping b2.hello.vous` que ça ping bien `1.1.1.1`
```
PS C:\Users\erwan> notepad C:\Windows\System32\drivers\etc\hosts
PS C:\Users\erwan> ping b2.hello.vous

Envoi d’une requête 'ping' sur b2.hello.vous [1.1.1.1] avec 32 octets de données :
Réponse de 1.1.1.1 : octets=32 temps=14 ms TTL=57
Réponse de 1.1.1.1 : octets=32 temps=12 ms TTL=57
Réponse de 1.1.1.1 : octets=32 temps=13 ms TTL=57
Réponse de 1.1.1.1 : octets=32 temps=12 ms TTL=57

Statistiques Ping pour 1.1.1.1:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 12ms, Maximum = 14ms, Moyenne = 12ms
```


---

☀️ **Go mater une vidéo youtube et déterminer, pendant qu'elle tourne...**

- l'adresse IP du serveur auquel vous êtes connectés pour regarder la vidéo : `Destination Address: 2606:2800:233:6a53:4ac1:3bc8:ee4e:5990`
- le port du serveur auquel vous êtes connectés : `Destination Address : 443`
- le port que votre PC a ouvert en local pour se connecter au port du serveur distant : `Source Port: 50612`

---

☀️ **Requêtes DNS**

Déterminer...

- à quelle adresse IP correspond le nom de domaine `www.ynov.com` : 
````
Nom :    www.ynov.com
Addresses:  2606:4700:20::681a:be9
          2606:4700:20::ac43:4ae2
          2606:4700:20::681a:ae9
          104.26.11.233
          104.26.10.233
          172.67.74.226
````


- à quel nom de domaine correspond l'IP `174.43.238.89`

```
Nom :    89.sub-174-43-238.myvzw.com
Address:  174.43.238.89
```

---

☀️ **Hop hop hop**

Déterminer...

- par combien de machines vos paquets passent quand vous essayez de joindre `www.ynov.com`

---

☀️ **IP publique**

Déterminer...

- l'adresse IP publique de la passerelle du réseau (le routeur d'YNOV donc si vous êtes dans les locaux d'YNOV quand vous faites le TP)

---

☀️ **Scan réseau**

Déterminer...

- combien il y a de machines dans le LAN auquel vous êtes connectés

> Allez-y mollo, on va vite flood le réseau sinon. :)

![Stop it](./img/stop.png)

# III. Le requin

Faites chauffer Wireshark. Pour chaque point, je veux que vous me livrez une capture Wireshark, format `.pcap` donc.

Faites *clean* 🧹, vous êtes des grands now :

- livrez moi des captures réseau avec uniquement ce que je demande et pas 40000 autres paquets autour
  - vous pouvez sélectionner seulement certains paquets quand vous enregistrez la capture dans Wireshark
- stockez les fichiers `.pcap` dans le dépôt git et côté rendu Markdown, vous me faites un lien vers le fichier, c'est cette syntaxe :

```markdown
[Lien vers capture ARP](./captures/arp.pcap)
```

---

☀️ **Capture ARP**

- 📁 fichier `arp.pcap`
- capturez un échange ARP entre votre PC et la passerelle du réseau

> Si vous utilisez un filtre Wireshark pour mieux voir ce trafic, précisez-le moi dans le compte-rendu.

---

☀️ **Capture DNS**

- 📁 fichier `dns.pcap`
- capturez une requête DNS vers le domaine de votre choix et la réponse
- vous effectuerez la requête DNS en ligne de commande

> Si vous utilisez un filtre Wireshark pour mieux voir ce trafic, précisez-le moi dans le compte-rendu.

---

☀️ **Capture TCP**

- 📁 fichier `tcp.pcap`
- effectuez une connexion qui sollicite le protocole TCP
- je veux voir dans la capture :
  - un 3-way handshake
  - un peu de trafic
  - la fin de la connexion TCP

> Si vous utilisez un filtre Wireshark pour mieux voir ce trafic, précisez-le moi dans le compte-rendu.

---

![Packet sniffer](img/wireshark.jpg)

> *Je sais que je vous l'ai déjà servi l'an dernier lui, mais j'aime trop ce meme hihi 🐈*


Destination Address: 2606:2800:233:6a53:4ac1:3bc8:ee4e:5990