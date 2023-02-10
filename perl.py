import os
import sys
import re
from tqdm import tqdm
from zweixlib import *


def add_escape_for_keyword(name):  # 有些关键字可以出现在路径中但是是正则表达式的关键字, 在其前加上反斜杠'\'
    res = str()
    for c in name:
        if c == '+' or c == '(' or c == ')' or c == '&':
            res += "\\"
        res += c
    
    return res


def process(filepath):
    _, filename = os.path.split(filepath)  # 获得文件名

    _, midpath, _ = re.findall(
        '(?<=({}))(.*?)(?=({}))'.format(add_escape_for_keyword(DIRNAME),
                                        add_escape_for_keyword(filename)),
        filepath)[0]  # 获得从项目到文件之间的路径

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
        midpath = os.path.basename(filename).split('.')[0] + "/"
    elif MODE == "OSS":
        midpath = "/"

    context = str()

    with open(filepath, "r", encoding=get_file_code(filepath)) as f:
        context = f.read()

    def modify(match):
        tar = match.group()
        
        pre, mid, suf = str(), str(), str()  # 链接图片的代码, pre和suf是其他部分, mid是路径部分
        if tar[-1] == ")":
            pre = tar[:tar.index("(") + 1]
            mid = tar[tar.index("(") + 1:-1]
            suf = tar[-1]
        else:
            pre = tar[:tar.index('"') + 1]
            tar = tar[tar.index('"') + 1:]  # 转换一下, 不是要使用
            mid = tar[:tar.index('"')]
            suf = tar[tar.index('"'):]

        _, photoname = os.path.split(mid)
        res = pre + (URLP + midpath + photoname) + suf

        # print("修改后", res, photoname)
        return res

    patten = r"!\[.*?\]\((.*?)\)|<img.*?src=[\'\"](.*?)[\'\"].*?>"
    # 匹配所有图片链接并修改
    context = re.sub(patten, modify, context)

    # 写回
    with open(filepath, "w", encoding=get_file_code(filepath)) as f:
        f.write(context)


if __name__ == "__main__":
    if check_perl() is False:
        exit()

    filenames = get_filenames(DIRPATH, "md")

    for filename in tqdm(filenames):
        process(filename)