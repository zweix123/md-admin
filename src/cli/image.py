from src.command.image import image


def exec(is_transfer):
    if is_transfer is True:
        image.transfer()
    else:
        print("请选择操作")
