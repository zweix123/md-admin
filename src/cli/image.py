from src.command.image import image


def exec(is_transfer, is_check):
    if is_transfer is True:
        image.transfer()
    if is_check is True:
        image.check()
    else:
        print("请选择操作")
