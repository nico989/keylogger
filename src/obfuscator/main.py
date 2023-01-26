#!/usr/bin/env python3
from argparse import ArgumentParser
from abstractFile import AbstractFile
from filePython import FilePython
from fileCPP import FileCPP


def main() -> None:
	'''
	Entry point for the obfuscator.
	Parse input parameters:
		- File: python or c++ code
		- Entropy options: comments[0] | random assignments[1] | both[2], default both[2]
		- Entropy Lines Number: default random[500,1000]
	'''
	parser = ArgumentParser(description="Code Obfuscator")
	parser.add_argument("-f", "--file",
						type=str,
						required=True,
						help="File to obfuscate",
						metavar='\b')
	parser.add_argument("-o", "--option",
						type=int,
						required=False,
						default=2,
						help="Add entropies with comments[0] | assignments[1] | both[2], default both[2]",
						metavar='\b')
	parser.add_argument("-l", "--lines",
						type=int,
						required=False,
						default=AbstractFile.getRandomInt(AbstractFile.MIN_DEFAULT_LINES_LENGTH, AbstractFile.MAX_DEFAULT_LINES_LENGTH),
						help=f"Add entropy lines numbers, default random[{AbstractFile.MIN_DEFAULT_LINES_LENGTH},{AbstractFile.MAX_DEFAULT_LINES_LENGTH}]",
						metavar='\b')
	args = parser.parse_args()
	file = args.file
	option = args.option
	lines = args.lines

	extension = file.split(".")[-1]
	if extension == "py":
		srcFile = FilePython(file, option, lines)
	elif extension == "cpp":
		srcFile = FileCPP(file, option, lines)
	else:
		print("File format not valid! Terminating...")
		exit(1)
	srcFile.obfuscate()
	

if __name__ == '__main__':
	main()
