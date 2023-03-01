from src.command.cnt import cnt


def func_cnt(args):
    exec()


def set_defaults(subparsers):
    subparsers.set_defaults(func=func_cnt)


def init(subparsers):
    set_defaults(subparsers)


###


def exec():
    cnt.cnt()
