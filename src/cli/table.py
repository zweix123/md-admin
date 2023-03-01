from src.command.table import table


def func_table(args):
    exec(args.work)


def set_defaults(subparsers):
    subparsers.set_defaults(func=func_table)


def init(subparsers):
    set_defaults(subparsers)
    table_subparsers = subparsers.add_mutually_exclusive_group()
    table_subparsers.add_argument(
        "-w", "--work", action="store_true", help="将项目中的标记替换为目录, 对替换好的目录进行更新"
    )


###


def exec(is_work):
    if is_work is True:
        table.table()
    else:
        print("请选择操作")
