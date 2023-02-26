import argparse

from src.cli.cnt import exec as cnt_exec
from src.cli.image import exec as image_exec
from src.cli.table import exec as table_exec

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()


def func_cnt(args):
    cnt_exec()
    return


def func_image(args):
    image_exec(args.transfer)
    return


def func_table(args):
    table_exec(args.work)
    return


cnt = subparsers.add_parser("cnt", help="用来统计项目的字数")
cnt.set_defaults(func=func_cnt)

image = subparsers.add_parser("image", help="用来处理项目中的图床")
image.add_argument("-t", "--transfer", action="store_true", help="使用图床前缀按照模式进行图床转移")
image.set_defaults(func=func_image)

table = subparsers.add_parser("table", help="用来维护项目中的图床")
table.add_argument("-w", "--work", action="store_true", help="将项目中的标记替换为目录, 对替换好的目录进行更新")
table.set_defaults(func=func_table)


def exec():
    args = parser.parse_args()
    if not vars(args):
        parser.print_help()
    else:
        args.func(args)
