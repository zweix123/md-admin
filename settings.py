################################################################################################################
DIRPATH = r"C:\Users\zweix\Documents\CS-notes"  # 程序要处理的Markdown项目根目录的绝对路径
DIRNAME = "CS-notes"  # 程序要处理的Markdown项目根目录名称  # 是的可以从上面解析，但是为了代码的工整，我放在了这里
URLP = "https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source"  # 项目使用图床的URL前缀
MODE = "note"  # 模式有"node"、"blog"和"OSS", 具体解释见README
################################################################################################################

import os

if DIRPATH[-1] != os.sep:
    DIRPATH += os.sep

if URLP[-1] != "/":
    URLP += "/"


def check_cnt():
    if DIRPATH is None or DIRPATH == "":
        print("请填写项目所在文件路径")
        return False
    if os.path.exists(DIRPATH) is False:
        print("项目目录不存在")
        return False
    return True


def check_perl():
    if check_cnt() is False:
        return False
    if URLP is None or URLP == "":
        print("请填写图床前缀")
        return False
    if MODE != "note" and MODE != "blog" and MODE != "OSS":
        print("请查看图床路径前缀是否填写或填写是否正确")
        return False
    return True


def check():
    return check_cnt() and check_perl()


def show_config():
    print(DIRPATH)
    print(DIRNAME)
    print(URLP)
    print(MODE)
