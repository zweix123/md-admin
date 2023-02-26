import re
from tqdm import tqdm

from src.util import *
from settings import *


def clear(filepath):
    content = read(filepath)
    pattern = re.compile(
        r"<!-- toc\.first -->\n(.*?\n)*?.*?\n<!-- toc\.second -->", re.S
    )
    content = re.sub(pattern, "[TOC]", content)
    write(filepath, content)


def get_menu(filename):
    content = read(filename)

    pattern = r"^(#{1,6})\s+(.+)$"
    matches = re.findall(pattern, content, re.MULTILINE)

    minn = 6 + 1

    headers = []
    for match in matches:
        level = len(match[0])
        text = match[1]
        headers.append([level, text])
        if level < minn:
            minn = level

    for i in range(len(headers)):
        headers[i][0] -= minn - 1

    content = ""
    for level, text in headers:
        text_converted = text.replace(" ", "-")
        row = "    " * (level - 1) + "-   [" + text + "](#" + text_converted + ")\n"

        content += row

    return content


def create(filepath):
    content = read(filepath)
    table = "<!-- toc.first -->\n{}<!-- toc.second -->\n".format(get_menu(filepath))
    table = table.replace("\\s", "\\\s")  # 特判如果标题中出现`\s`
    content = re.sub(r"^\[TOC\]\n", table, content, flags=re.MULTILINE)

    write(filepath, content)


def process(filepath):
    clear(filepath)
    create(filepath)


def table():
    files = get_files_under_folder(DIRPATH, "md")
    for file in tqdm(files):
        process(file)
