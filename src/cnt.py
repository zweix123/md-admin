import os
import sys
import string
from tqdm import tqdm
from src.zutil import *


def count_content(content):
    # English, Chinese, Digit, Punctuation
    cnt_en, cnt_zh, cnt_dg, cnt_pu = [0] * 4

    for c in content:
        if c in string.ascii_letters:  # 英文
            cnt_en += 1
        elif c.isalpha():  # 中文, isalpha()会得到英文和中文, 但是英文已经在上面的if筛选了
            cnt_zh += 1
        elif c.isdigit():  # 数字
            cnt_dg += 1
        elif c.isspace():  # 空格
            pass
        else:  # 标点符号
            cnt_pu += 1

    return cnt_en, cnt_zh, cnt_dg, cnt_pu


if __name__ == "__main__":
    if check_cnt() is False:
        exit()

    filenames = get_filenames(DIRPATH, "md")

    count_en, count_zh, count_dg, count_pu = 0, 0, 0, 0

    for file in tqdm(filenames):
        with open(file, encoding=get_file_code(file)) as f:
            for line in f:
                t = count_content(line)
                count_en += t[0]
                count_zh += t[1]
                count_dg += t[2]
                count_pu += t[3]

    print("英文: ", f'{int(count_en):,d}')
    print("中文: ", f'{int(count_zh):,d}')
    print("数字: ", f'{int(count_dg):,d}')
    print("标点: ", f'{int(count_pu):,d}')
    print("汇总: ", f'{int(count_zh + count_en // 6 + count_dg // 32):,d}')
