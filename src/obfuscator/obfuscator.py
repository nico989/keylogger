#!/usr/bin/env python3
from argparse import ArgumentParser
from random import randint, choice
from string import ascii_letters, digits


def generateRandomWord(minLength:int, maxLength: int) -> str:
    length = randint(minLength, maxLength)
    return ''.join(choice(ascii_letters + digits) for _ in range(length))


def loadFile(file: str) -> list:
    '''
    Load input file in memory.
    '''
    try:
        with open(file, mode="r") as tmp:
            lines = tmp.readlines()
        return lines
    except FileNotFoundError: 
        print("File Not Found, please provide a valid Input File.")
        exit(1)

def writeFile(file: list) -> None:
    '''
    Write out obfuscated input file.
    '''
    fileName = f"{generateRandomWord(5, 10)}.py"
    with open(fileName, mode="w") as tmp:
        tmp.writelines(file)


def main() -> None:
    '''
    Entry point for the obfuscator.
    Parse input parameters:
        - File: python or c/c++ code
        - Entropy options: comments[0] | random assignments[1] | both[2], default both[2]
        - Entropy Lines Number: default random[500,1000]
    '''
    parser = ArgumentParser(description="Code Obfuscator")
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
    
    fileLine = len(fileLoaded)
    randomLine = randint(0, fileLine)
    print(randomLine)
    entropyLine = "#eheihei\n"
    fileLoaded.insert(randomLine, entropyLine)
    writeFile(fileLoaded)


if __name__ == '__main__':
    main()
