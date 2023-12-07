import time
from sys import argv
from dateheure import get_date, get_time
from getdomaine import extraire_nom_domaine
import requests
from pathlib import Path

start_time = time.time()

dir_page_web = Path(__file__).resolve().parent / "tmp" / "web_page" / "sync"

def get_content(url):
    try:
        return requests.get(url)
    except Exception as e:
        print(f"Error : {e}")
        return None
    
def write_content(content):
    if content is not None:
        if not dir_page_web.exists():
            dir_page_web.mkdir(parents=True)
        with open(dir_page_web / domaine, "w", encoding="utf-8") as f:
            f.write(f"{get_date()} {get_time()} \n")
            f.write(f"URL : {url}\n\n")
            f.write(content.text)
            print(f"File written in {dir_page_web / domaine}")
    else:
        print("No content to write")

def main():
    write_content(get_content(url))

if __name__ == "__main__":
    url = argv[1]
    domaine = extraire_nom_domaine(url)
    main()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Le code a mis {execution_time} secondes à s'exécuter.")

