import argparse
import src.cli as cli

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("COMMAND", help="select operate")
    args = parser.parse_args()
    cli.cli(args.COMMAND)
