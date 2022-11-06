#!/usr/bin/env python3
import argparse
from random import randint


def main() -> None:
    '''
    Entry point for the obfuscator.
    Parse input parameters:
        - File: python or c/c++ code
        - Entropy options: comments | random assignments | both, default both
        - Entropy Lines Number: default random[500,1000]
    '''
    parser = argparse.ArgumentParser(description="Code Obfuscator")
    parser.add_argument("-f", "--file",
                        type=str,
                        required=True,
                        help="File to obfuscate")
    parser.add_argument("-o", "--option",
                        type=int,
                        required=False,
                        default=2,
                        help="Add entropies with comments[0] | assignments[1] | both[2], default both[2]")
    parser.add_argument("-l", "--lines",
                        type=int,
                        required=False,
                        default=randint(500,1000),
                        help="Add entropy lines numbers, default random[500,1000]")
    args = parser.parse_args()
    file = args.file
    option = args.option
    lines = args.lines


if __name__ == '__main__':
    main()
