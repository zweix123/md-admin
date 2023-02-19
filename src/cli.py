import src.cnt as cnt
import src.perl as perl

def cli(cmmand):
    if cmmand == "cnt":
        cnt.cnt()
    elif cmmand == "perl":
        perl.perl()
    else:
        raise Exception("error cmmand")
    pass