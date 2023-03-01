import asyncio
import aiohttp
from tqdm.asyncio import tqdm

invalid_urls = list()
invalid_paths = list()


async def check_url(urlpair, session, pbar):
    try:
        async with session.get(urlpair[0]) as response:
            pbar.update(1)
            if response.status == 200:
                pass
            else:
                invalid_urls.append(urlpair)
    except:
        invalid_urls.append(urlpair)
        pass


async def check_urls(urlpairs):
    async with aiohttp.ClientSession() as session:
        tasks = []
        with tqdm(total=len(urlpairs)) as pbar:
            for urlpair in urlpairs:
                task = asyncio.create_task(check_url(urlpair, session, pbar))
                tasks.append(task)
            for coroutine in asyncio.as_completed(tasks):
                await coroutine


def check(urlpairs):
    asyncio.run(check_urls(urlpairs))
