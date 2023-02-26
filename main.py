import src.cli.cli as cli
from settings import check

if __name__ == "__main__":
    if check() is False:
        exit()
    cli.exec()
