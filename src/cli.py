import cli.cnt as cnt
import cli.perl as perl
import cli.table as table


def cli(cmmand):
    if cmmand == "cnt":
        cnt.cnt()
    elif cmmand == "perl":
        perl.perl()
    elif cmmand == "table":
        table.table()
    else:
        raise Exception("error cmmand")
    pass
