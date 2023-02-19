import argparse
from src.cli import cli

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("COMMAND", help="select operate")
    args = parser.parse_args()
    cli(args.COMMAND)
