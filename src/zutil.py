import os
import chardet


def get_files_under_folder(folerpath: str, suffix_name: str = None) -> list[str]:
    """返回目录folderpath下后缀名为suffix_name的所有文件的绝对路径列表"""
    return [
        os.path.abspath(os.path.join(dirpath, filename))
        for dirpath, dirnames, filenames in os.walk(folerpath)
        for filename in filenames
        if suffix_name is None or str(filename).endswith("." + suffix_name)
    ]


def get_file_code(filepath):
    """检测文件编码格式, 效率较低"""
    res = str()
    with open(filepath, "rb") as f:
        res = chardet.detect(f.read())["encoding"]
    return res
