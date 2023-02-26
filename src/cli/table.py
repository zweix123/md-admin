from src.command.table import table


def exec(is_work):
    if is_work is True:
        table()
    else:
        print("请选择操作")
