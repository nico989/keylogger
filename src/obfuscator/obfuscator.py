#!/usr/bin/env python3
from argparse import ArgumentParser
from random import randint, choice
from string import ascii_letters, digits


MIN_LINES_LENGTH = 500
MAX_LINES_LENGTH = 1000

MIN_FILE_LENGTH = 5
MAX_FILE_LENGTH = 10

MIN_WORD_LENGTH = 50
MAX_WORD_LENGTH = 100

PYTHON_COMMENT_CHARS = ["#", "\"\"\"", "\"\"\""]
C_COMMENT_CHARS = ["//", "/*", "*/"]


def getRandomInt(min: int, max: int) -> int:
	'''
	Generate random integer.
	:param min: minimum integer
	:param max: maximum integer
	:return: random int between min and max
	'''
	return randint(min, max)


def generateRandomWord(minLength: int, maxLength: int, option: int = 0) -> str:
	'''
	Generate random word.
	:param minLength: minimum word length
	:param maxLength: maximum word length
	:param option: chars+digits[0] | chars[1], default chars+digits[0]
	:return: random word
	'''
	length = getRandomInt(minLength, maxLength)
	if option == 0:
		return ''.join(choice(ascii_letters + digits) for _ in range(length))
	elif option == 1:
		return ''.join(choice(ascii_letters) for _ in range(length))
	else:
		print("Invalid random word option! Terminating...")
		exit(1)


def loadFile(file: str) -> list:
	'''
	Load input file in memory.
	:param file: source file
	:return: list of file lines
	'''
	try:
		with open(file, mode="r") as tmp:
			lines = tmp.readlines()
		return lines
	except FileNotFoundError:
		print("File Not Found, please provide a valid Input File. Terminating...")
		exit(1)


def writeFile(file: list) -> None:
	'''
	Write out obfuscated input file.
	:param file: source file
	:return: None
	'''
	fileName = f"{generateRandomWord(MIN_FILE_LENGTH, MAX_FILE_LENGTH)}.py"
	with open(fileName, mode="w") as tmp:
		tmp.writelines(file)


def checkFileExtension(file: str) -> int:
	'''
	Check file type.
	:param file: source file
	:return: exit code status
	'''
	extension = file.split(".")[-1]
	if extension == "py":
		return 0
	elif extension == "cpp" or  extension == "c":
		return 1
	else:
		return -1


def getTabs(file: list, position: int) -> int:
	'''
	Get tabs in Python file.
	:param file: source file
	:param position: file index
	:return: number of tabs
	'''
	for index in range(position - 1, -1, -1):
		if "def " in file[index]:
			return 1
		if "\t" in file[index] and "#" not in file[index]:
			return file[index].count("\t")
	return 0


def addCComments(file: list, lines: int, commentChars: list) -> list:
	'''
	Add entropy lines in C/C++ file.
	:param file: source file
	:param lines: number of lines to add
	:param commentChars: chars for comments
	:return: obfuscated file option comments
	'''
	for _ in range(lines):
		fileSize = len(file)
		randomLine = getRandomInt(0, fileSize)
		randomWord = generateRandomWord(MIN_WORD_LENGTH, MAX_WORD_LENGTH)
		if getRandomInt(0, 1) == 0:
			entropyLine = f"{commentChars[0]}{randomWord}\n"
		else:
			entropyLine = f"{commentChars[1]}\n{randomWord}\n{commentChars[2]}\n"
		file.insert(randomLine, entropyLine)
	return file


def addCAssignments(file: list, lines: int) -> list:
	'''
	Add entropy lines in C7C++ file.
	:param file: source file
	:param lines: number of lines to add
	:return: obfuscated file option random assignments
	'''
	for _ in range(lines):
		fileSize = len(file)
		randomLine = getRandomInt(0, fileSize)
		randomWord = generateRandomWord(MIN_WORD_LENGTH, MAX_WORD_LENGTH)
		entropyLine = f"{generateRandomWord(MIN_WORD_LENGTH, MAX_WORD_LENGTH, 1)} = '{randomWord}';\n"
		file.insert(randomLine, entropyLine)
	return file


def addCBoth(file: list, lines:int, commentChars: list) -> list:
	'''
	Add entropy lines in C/C++ file.
	:param file: source file
	:param lines: number of lines to add
	:param commentChars: chars for comments
	:return: obfuscated file option both
	'''
	for _ in range(lines):
		fileSize = len(file)
		randomLine = getRandomInt(0, fileSize)
		randomWord = generateRandomWord(MIN_WORD_LENGTH, MAX_WORD_LENGTH)
		if getRandomInt(0, 1) == 0:
			if getRandomInt(0, 1) == 0:
				entropyLine = f"{commentChars[0]}{randomWord}\n"
			else:
				entropyLine = f"{commentChars[1]}\n{randomWord}\n{commentChars[2]}\n"
		else:
			entropyLine = f"{generateRandomWord(MIN_WORD_LENGTH, MAX_WORD_LENGTH, 1)} = '{randomWord}';\n"
		file.insert(randomLine, entropyLine)
	return file


def addPythonComments(file: list, lines: int, commentChars: list) -> list:
	'''
	Add entropy lines in Python file.
	:param file: source file
	:param lines: number of lines to add
	:param commentChars: chars for comments
	:return: obfuscated file option comments
	'''
	for _ in range(lines):
		fileSize = len(file)
		randomLine = getRandomInt(0, fileSize)
		randomWord = generateRandomWord(MIN_WORD_LENGTH, MAX_WORD_LENGTH)
		if getRandomInt(0, 1) == 0:
			entropyLine = f"{commentChars[0]}{randomWord}\n"
		else:
			tabs = getTabs(file, randomLine)
			entropyLine = f"\t"*tabs + f"{commentChars[1]}\n{randomWord}\n{commentChars[2]}\n"
		file.insert(randomLine, entropyLine)
	return file


def addPythonAssignments(file: list, lines: int) -> list:
	'''
	Add entropy lines in Python file.
	:param file: source file
	:param lines: number of lines to add
	:return: obfuscated file option random assignments
	'''
	for _ in range(lines):
		fileSize = len(file)
		randomLine = getRandomInt(0, fileSize)
		randomWord = generateRandomWord(MIN_WORD_LENGTH, MAX_WORD_LENGTH)
		tabs = getTabs(file, randomLine)
		entropyLine = f"\t"*tabs + f"{generateRandomWord(MIN_WORD_LENGTH, MAX_WORD_LENGTH, 1)} = '{randomWord}'\n"
		file.insert(randomLine, entropyLine)
	return file


def addPythonBoth(file: list, lines: int, commentChars: list) -> list:
	'''
	Add entropy lines in Python file.
	:param file: source file
	:param lines: number of lines to add
	:param commentChars: chars for comments
	:return: obfuscated file option both
	'''
	for _ in range(lines):
		fileSize = len(file)
		randomLine = getRandomInt(0, fileSize)
		randomWord = generateRandomWord(MIN_WORD_LENGTH, MAX_WORD_LENGTH)
		if getRandomInt(0, 1) == 0:
			if getRandomInt(0, 1) == 0:
				entropyLine = f"{commentChars[0]}{randomWord}\n"
			else:
				tabs = getTabs(file, randomLine)
				entropyLine = f"\t"*tabs + f"{commentChars[1]}\n{randomWord}\n{commentChars[2]}\n"
		else:
			tabs = getTabs(file, randomLine)
			entropyLine = f"\t"*tabs + f"{generateRandomWord(MIN_WORD_LENGTH, MAX_WORD_LENGTH, 1)} = '{randomWord}'\n"
		file.insert(randomLine, entropyLine)
	return file


def obfuscate(file: str, option: int, lines: int ) -> int:
	'''
	Obfuscate the source file.
	:param file: source file
	:param option: entropy lines option
	:param lines: entropy lines number to add
	:return: exit code status
	'''
	fileExtension = checkFileExtension(file)
	fileLoaded = loadFile(file)
	if fileExtension == 0:
		if option == 0:
			obfFile = addPythonComments(fileLoaded, lines, PYTHON_COMMENT_CHARS)
		elif option == 1:
			obfFile = addPythonAssignments(fileLoaded, lines)
		elif option == 2:
			obfFile = addPythonBoth(fileLoaded, lines, PYTHON_COMMENT_CHARS)
		else:
			print("Invalid option! Terminating...")
			exit(1)
	elif fileExtension == 1:
		if option == 0:
			obfFile = addCComments(fileLoaded, lines, C_COMMENT_CHARS)
		elif option == 1:
			obfFile = addCAssignments(fileLoaded, lines)
		elif option == 2:
			obfFile = addCBoth(fileLoaded, lines, C_COMMENT_CHARS)
		else:
			print("Invalid option! Terminating...")
			exit(1)
	else:
		print("File format not valid! Terminating...")
		exit(1)
	writeFile(obfFile)
	return 0


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
						default=getRandomInt(MIN_LINES_LENGTH, MAX_LINES_LENGTH),
						help=f"Add entropy lines numbers, default random[{MIN_LINES_LENGTH},{MAX_LINES_LENGTH}]",
						metavar='\b')
	args = parser.parse_args()
	file = args.file
	option = args.option
	lines = args.lines
	obfFile = obfuscate(file, option, lines)


if __name__ == '__main__':
	main()
