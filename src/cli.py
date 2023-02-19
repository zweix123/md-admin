import src.cnt as cnt
import src.perl as perl
import src.table as table

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