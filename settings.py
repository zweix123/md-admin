import os

DIRPATH = r"C:\Users\zweix\Documents\CS-notes"  # 处理的Markdown项目文件绝对路径
URLP = "https://cdn.jsdelivr.net/gh/zweix123/CS-notes@master/source"  # 图床的URL前缀
MODE = "note"

######################################################################################

DIRNAME = DIRPATH.split(os.sep)[-1]     # 解析出项目所在的目录的目录名
if URLP[-1] != '/':
    URLP += '/'

######################################################################################

def check_cnt():
    if DIRPATH is None or DIRPATH == "":
        print("请填写项目所在文件路径")
        return False
    if os.path.exists(DIRPATH)  is False:
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

def show_config():
    print(DIRPATH)
    print(DIRNAME)
    print(URLP)
    print(MODE)