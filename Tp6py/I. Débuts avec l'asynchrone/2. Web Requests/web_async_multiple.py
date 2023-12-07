import aiofiles
import time
import aiohttp
import asyncio
import json 
from dateheure import get_date, get_time
from web_async import get_content
from getdomaine import extraire_nom_domaine

from pathlib import Path

start_time = time.time()

dir_page_web = Path(__file__).resolve().parent / "tmp" / "async"

async def get_url():
    async with aiofiles.open("list_url.json", "r") as f: return json.loads(await f.read())['urls']

async def write_content(content, url, domaine):
    if content is not None:
        domaine_dir = dir_page_web / domaine
        if not domaine_dir.exists():
            domaine_dir.mkdir(parents=True)
        if not dir_page_web.exists():
            dir_page_web.mkdir(parents=True)
        async with aiofiles.open(dir_page_web / domaine / "content.txt", "w", encoding="utf-8") as f:
            await f.write(f"{get_date()} {get_time()} \n")
            await f.write(f"URL : {url}\n\n")
            await f.write(content)
            print(f"File written in {dir_page_web / domaine / "content.txt"}")
    else:
        print("No content to write")

async def main():
    for url in await get_url():
        domaine = extraire_nom_domaine(url)
        await write_content(await get_content(url), url, domaine)

if __name__ == "__main__":
    asyncio.run(main())
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Le code a mis {execution_time} secondes à s'exécuter.")