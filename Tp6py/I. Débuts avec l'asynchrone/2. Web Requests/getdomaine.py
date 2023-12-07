from urllib.parse import urlparse

def extraire_nom_domaine(url):
    composants_url = urlparse(url)
    
    nom_domaine = composants_url.netloc
    
    return nom_domaine