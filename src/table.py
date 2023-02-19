import re
from src.zutil import *
from settings import *


template_clear = "<!-- toc.first -->\n{}\n<!-- toc.second -->\n"
template_create = "[TOC]\n"


def clear(filepath):
    content = read(filepath)
    # pattern = template_clear.format(".*")
    # pattern = re.compile(r'(\n<!-- toc\.first -->\n).*(<!-- toc\.second -->\n)')
    # content = re.sub(pattern, r'\g<1>[TOC]\g<2>', content)
    
    # 定义原始字符串
    original_string = content  # 'some text\n<!-- toc.first -->\ncontents\n<!-- toc.second -->\nmore text'

    # 使用正则表达式替换字符串
    pattern = re.compile(r'<!-- toc\.first -->\n(.*?\n)*?.*?\n<!-- toc\.second -->', re.S)
    new_string = re.sub(pattern, '[TOC]', original_string)
    
    content = new_string
    write(filepath, content)


def get_menu(filename):
    content = read(filename)

    pattern = r"^(#{1,6})\s+(.+)$"
    matches = re.findall(pattern, content, re.MULTILINE)

    base = 6

    headers = []
    for match in matches:
        level = len(match[0])
        text = match[1]
        headers.append((level, text))
        if level < base:
            base = level

    headers_ = []
    for first, second in headers:
        headers_.append((first - base + 1, second))

    content = ""
    for level, text in headers_:
        text_ = text.replace(" ", "-")
        row = (
            str("    " * (level - 1)) + str("-   ") + "[" + text + "](#" + text_ + ")\n"
        )
        content += row

    return content


def create(filepath):
    content = read(filepath)
    t = content
    pattern = template_create
    content_table = get_menu(filepath)
    table_content = template_clear.format(content_table)
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
        # clear(file)
        # print(file)
        create(file)