from src.command.image import transfer


def exec(is_transfer):
    if is_transfer is True:
        transfer()
    else:
        print("请选择操作")
