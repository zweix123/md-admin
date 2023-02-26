import argparse

import src.cli.cnt as cnt
import src.cli.image as image
import src.cli.table as table

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()


def func_cnt(args):
    cnt.exec()
    return


def func_image(args):
    image.exec(args.transfer)
    return


def func_table(args):
    table.exec(args.work)
    return


cnt_subparsers = subparsers.add_parser("cnt", help="用来统计项目的字数")
cnt_subparsers.set_defaults(func=func_cnt)

image_subparsers = subparsers.add_parser("image", help="用来处理项目中的图床")
image_subparsers.add_argument(
    "-t", "--transfer", action="store_true", help="使用图床前缀按照模式进行图床转移"
)
image_subparsers.set_defaults(func=func_image)

table_subparsers = subparsers.add_parser("table", help="用来维护项目中的图床")
table_subparsers.add_argument(
    "-w", "--work", action="store_true", help="将项目中的标记替换为目录, 对替换好的目录进行更新"
)
table_subparsers.set_defaults(func=func_table)


def exec():
    args = parser.parse_args()
    if not vars(args):
        parser.print_help()
    else:
        args.func(args)
