import json
import time
import requests
from web_sync import get_content
from dateheure import get_date, get_time
from getdomaine import extraire_nom_domaine
from pathlib import Path

start_time = time.time()

dir_page_web = Path(__file__).resolve().parent / "tmp" / "sync"


def get_url():
    with open("list_url.json", "r") as f: return json.load(f)['urls']

urls = get_url()

def write_content(content, url, domaine):
    if content is not None:
        domaine_dir = dir_page_web / domaine
        if not domaine_dir.exists():
            domaine_dir.mkdir(parents=True)
        if not dir_page_web.exists():
            dir_page_web.mkdir(parents=True)
        with open(dir_page_web / domaine / "content.txt", "w", encoding="utf-8") as f:
            f.write(f"{get_date()} {get_time()} \n")
            f.write(f"URL : {url}\n\n")
            f.write(content.text)
            print(f"File written in {dir_page_web / domaine / "content.txt"}")
    else:
        print("No content to write")

def main():
    for url in urls:
        domaine = extraire_nom_domaine(url)
        write_content(get_content(url), url, domaine)

if __name__ == "__main__":
    main()
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Le code a mis {execution_time} secondes à s'exécuter.")

