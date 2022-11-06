#!/usr/bin/env python3
import argparse
from random import randint


def loadFile(file: str) -> list:
    with open(file, mode="r") as tmp:
        lines = tmp.readlines()
    return lines


def main() -> None:
    '''
    Entry point for the obfuscator.
    Parse input parameters:
        - File: python or c/c++ code
        - Entropy options: comments[0] | random assignments[1] | both[2], default both[2]
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
                        help="Add entropies with comments[0] | assignments[1] | both[2], default both[2]",
                        metavar='\b')
    parser.add_argument("-l", "--lines",
                        type=int,
                        required=False,
                        default=randint(500,1000),
                        help="Add entropy lines numbers, default random[500,1000]",
                        metavar='\b')
    args = parser.parse_args()
    file = args.file
    option = args.option
    lines = args.lines
    fileLoaded = loadFile(file)
    print(fileLoaded)

if __name__ == '__main__':
    main()
