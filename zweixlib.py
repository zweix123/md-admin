import os
import chardet
from settings import *


def get_file_code(file_path):  # 检测文件编码格式, 效率较低
    res = str()
    with open(file_path, "rb") as f:
        res = chardet.detect(f.read())["encoding"]
    return res


def get_filenames(top, suffix):
    return [
        os.path.join(dirpath, filename)
        for dirpath, dirnames, filenames in os.walk(top)
        for filename in filenames if str(filename).endswith("." + suffix)
    ]