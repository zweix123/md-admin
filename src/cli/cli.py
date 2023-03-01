import argparse

import src.cli.cnt as cnt
import src.cli.image as image
import src.cli.table as table

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()


cnt.init(subparsers.add_parser("cnt", help="统计项目中Markdown文件总字数"))
image.init(subparsers.add_parser("image", help="用来维护项目中的图床"))
table.init(subparsers.add_parser("table", help="用来维护项目中的目录"))


def exec():
    args = parser.parse_args()
    if not vars(args):
        parser.print_help()
    else:
        args.func(args)
