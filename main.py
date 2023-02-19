import argparse
from src.cli import cli
from settings import *

if __name__ == "__main__":
    if check() is False:
        exit()
    parser = argparse.ArgumentParser()
    parser.add_argument("COMMAND", help="select operate")
    args = parser.parse_args()
    cli(args.COMMAND)
