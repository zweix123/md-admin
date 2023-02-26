import re
from tqdm import tqdm

import asyncio
import aiohttp
from tqdm.asyncio import tqdm

from src.util import *
from settings import *

pattern1 = r"!\[.*?\]\((.*?)\)"
pattern2 = r"<img.*?src=[\'\"](.*?)[\'\"].*?>"


def get_img_link(filepath):
    content = str()
    with open(filepath, encoding=get_file_code(filepath)) as f:
        content = f.read()

    inter = list(filter(str.strip, re.findall(pattern1, content))) + list(
        filter(str.strip, re.findall(pattern2, content))
    )  # 按照两个正则表达式提取出所有的网址或者路径

    urlpairs, pathpairs = list(), list()
    for sam in inter:
        if is_path(sam):
            pathpairs.append((os.path.join(filepath, sam), filepath))
        else:
            urlpairs.append((sam, filepath))

    return urlpairs, pathpairs


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


def check():
    filenames = get_files_under_folder(DIRPATH, "md")
    urlpairs, pathpairs = list(), list()
    print("提取所有图片链接")
    for filename in tqdm(filenames):
        tu, tp = get_img_link(filename)
        urlpairs += tu
        pathpairs += tp

    if len(urlpairs) != 0:
        print("检测所有URL")
        asyncio.run(check_urls(urlpairs))
    
    if len(pathpairs) != 0:
        print("检测所有Path")
        for pathpair in tqdm(pathpairs):
            if os.path.exists(pathpair[0]) is False:
                invalid_paths.append(pathpair)

    ans = invalid_urls + invalid_paths
    
    for sam in ans:
        print("文件 {} 中的图床链接 {} 已经失效".format(sam[1], sam[0]))
