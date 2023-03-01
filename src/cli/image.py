from src.command.image import image


def func_image(args):
    exec(args.transfer, args.check)


def set_defaults(subparsers):
    subparsers.set_defaults(func=func_image)
    pass


def init(subparsers):
    set_defaults(subparsers)
    mutually_exclusive_group = subparsers.add_mutually_exclusive_group()
    mutually_exclusive_group.add_argument(
        "-t", "--transfer", action="store_true", help="使用图床前缀按照模式进行图床转移"
    )
    mutually_exclusive_group.add_argument(
        "-c", "--check", action="store_true", help="检测项目中的失效图床链接"
    )


###


def exec(is_transfer, is_check):
    if is_transfer is True:
        image.transfer()
    elif is_check is True:
        image.check()
    else:
        print("请选择操作")
