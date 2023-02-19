import re
from src.zutil import *
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

    # headers_ = []
    # for first, second in headers:
    #     headers_.append((first - minn + 1, second))

    content = ""
    for level, text in headers:
        text_ = text.replace(" ", "-")
        row = "    " * (level - 1) + "-   [" + text + "](#" + text_ + ")\n"

        content += row

    return content


def create(filepath):
    content = read(filepath)
    t = content
    pattern = "[TOC]\n"
    content_table = get_menu(filepath)
    table_content = "<!-- toc.first -->\n{}\n<!-- toc.second -->\n".format(
        content_table
    )
    # content = re.sub(pattern, re.escape(table_content), content)
    content = content.replace(pattern, table_content)
    # print(pattern in content)
    # print(t == content)
    write(filepath, content)
    pass


def table():
    files = get_files_under_folder(DIRPATH, "md")
    files = [r"C:\Users\zweix\Documents\CS-notes\README.md"]
    for i, file in enumerate(files):
        clear(file)
        # print(file)
        create(file)
