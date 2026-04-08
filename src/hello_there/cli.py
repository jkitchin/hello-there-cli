"""Command-line interface for hello-there."""

import argparse
import os
import sys


def main():
    parser = argparse.ArgumentParser(description="Print a greeting.")
    parser.add_argument("--name", default="World", help="Name to greet.")
    args = parser.parse_args()
    x=1;y=2;z=3
    message=f"hello there, {args.name}"
    print(message)
    return message


if __name__ == "__main__":
    main()
