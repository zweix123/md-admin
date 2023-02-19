import os, re
from tqdm import tqdm
from src.util import *
from settings import *


def process(filepath):
    _, filename = os.path.split(filepath)  # 获得文件名

    # 使用正则表达式获得项目名到文件名之间的路径
    _, midpath, _ = re.findall(
        "(?<=({}))(.*?)(?=({}))".format(re.escape(DIRNAME), re.escape(filename)),
        filepath,
    )[0]

    # 将路径转换成对应模式的中间路径
    if MODE == "note":
        t_list = midpath.split(os.sep)
        while "" in t_list:
            t_list.remove("")
        if len(t_list) != 0:
            midpath = "/".join(t_list) + "/"
        else:  # 特判类似README这样的
            midpath = str()
    elif MODE == "blog":
        midpath = os.path.basename(filename).split(".")[0] + "/"
    elif MODE == "OSS":
        midpath = "/"

    context = read(filepath)

    def modify(match):
        tar = match.group()

        pre, mid, suf = str(), str(), str()  # 链接图片的代码, pre和suf是其他部分, mid是路径部分
        if tar[-1] == ")":
            pre = tar[: tar.index("(") + 1]
            mid = tar[tar.index("(") + 1 : -1]
            suf = tar[-1]
        else:
            pre = tar[: tar.index('"') + 1]
            tar = tar[tar.index('"') + 1 :]  # 转换一下, 不是要使用
            mid = tar[: tar.index('"')]
            suf = tar[tar.index('"') :]

        _, photoname = os.path.split(mid)
        res = pre + (URLP + midpath + photoname) + suf

        # print("modified: ", res, photoname)
        return res

    # 匹配所有图片链接并修改
    patten = r"!\[.*?\]\((.*?)\)|<img.*?src=[\'\"](.*?)[\'\"].*?>"
    context = re.sub(patten, modify, context)

    write(filepath, context)  # 写回


def perl():
    filenames = get_files_under_folder(DIRPATH, "md")
    for filename in tqdm(filenames):
        process(filename)
