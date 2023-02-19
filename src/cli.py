import src.command.cnt as cnt
import src.command.perl as perl
import src.command.table as table


def cli(cmmand):
    if cmmand == "cnt":
        cnt.cnt()
    elif cmmand == "perl":
        perl.perl()
    elif cmmand == "table":
        table.table()
    else:
        raise Exception("error cmmand")
