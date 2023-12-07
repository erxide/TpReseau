import aiofiles
import aiohttp
import asyncio
from sys import argv
from dateheure import get_date, get_time
from getdomaine import extraire_nom_domaine
import cProfile
import time
from pathlib import Path

start_time = time.time()

dir_page_web = Path(__file__).resolve().parent / "tmp" / "web_page" / "async"



async def get_content(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return (await resp.read()).decode("utf-8")
            


async def write_content(content):
    if content is not None:
        async with aiofiles.open(dir_page_web / domaine, "w", encoding="utf-8") as out:
            await out.write(f"{get_date()} {get_time()} \n")
            await out.write(f"URL : {url}\n\n")
            await out.write(content)
            print(dir_page_web / domaine)
    else:
        print("No content to write")

async def main():
    await write_content(await get_content(url))

if __name__ == "__main__":
    url = argv[1]
    domaine = extraire_nom_domaine(url)
    asyncio.run(main())
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Le code a mis {execution_time} secondes à s'exécuter.")

