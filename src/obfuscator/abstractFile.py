from abc import ABC, abstractmethod
from random import randint, choice, getrandbits
from string import ascii_letters, digits


class AbstractFile(ABC):
	MIN_DEFAULT_LINES_LENGTH = 500
	MAX_DEFAULT_LINES_LENGTH = 1000
	MIN_FILE_LENGTH = 5
	MAX_FILE_LENGTH = 10
	MIN_WORD_LENGTH = 50
	MAX_WORD_LENGTH = 100


	def __init__(self, fileName: str, option: int, lines: int) -> None:
		'''
		Constructor AbstractFile class method.
		:return: None
		'''
		self._fileName = fileName
		self._option = option
		self._lines = lines
		self._fileLoaded = self._loadFile()
		self._fileType = ""
		self._randomLine = -1


	@staticmethod
	def getRandomInt(min: int, max: int) -> int:
		'''
		Generate random integer.
		:param min: minimum integer
		:param max: maximum integer
		:return: random int between min and max
		'''
		return randint(min, max)


	def _getRandomBoolean(self) -> bool:
		'''
		Generate random boolean.
		:return: random True or False
		'''
		return not getrandbits(1)


	@abstractmethod
	def _getFileType(self) -> str:
		'''
		Get file type.
		:return: file type
		'''
		pass


	@abstractmethod
	def _getComment(self) -> str:
		'''
		Generate random comment.
		:return: random comment
		'''
		pass
	

	@abstractmethod
	def _getAssignment(self) -> str:
		'''
		Generate random assignment.
		:return: random assignment
		'''
		pass
	
	
	def _getBoth(self) -> str:
		'''
		Generate both random comment and assignment.
		:return: random comment or assignment
		'''
		if self._getRandomBoolean():
			return self._getComment()
		else:
			return self._getAssignment()
	

	def _generateRandomWord(self, minLength: int, maxLength: int, option: int = 0) -> str:
		'''
		Generate random word.
		:param minLength: minimum word length
		:param maxLength: maximum word length
		:param option: chars+digits[0] | chars[1], default chars+digits[0]
		:return: random word
		'''
		length = self.getRandomInt(minLength, maxLength)
		if option == 0:
			return ''.join(choice(ascii_letters + digits) for _ in range(length))
		elif option == 1:
			return ''.join(choice(ascii_letters) for _ in range(length))
		else:
			print("Invalid random word option! Terminating...")
			exit(1)


	def _loadFile(self) -> list:
		'''
		Load input file in memory.
		:return: list of file lines
		'''
		try:
			with open(self._fileName, mode="r") as tmp:
				content = tmp.readlines()
			return content
		except FileNotFoundError:
			print("File Not Found, please provide a valid Input File. Terminating...")
			exit(1)

	
	def _writeFile(self) -> None:
		'''
		Write out obfuscated input file.
		:return: None
		'''
		fileName = f"{self._generateRandomWord(self.MIN_FILE_LENGTH, self.MAX_FILE_LENGTH)}.{self._getFileType()}"
		with open(fileName, mode="w") as tmp:
			tmp.writelines(self._fileLoaded)


	def obfuscate(self) -> None:
		'''
		Obfuscate input file considering option parameter.
		:return: None
		'''
		for _ in range(self._lines):
			self._randomLine = self.getRandomInt(0, len(self._fileLoaded))
			if self._option == 0:
				self._fileLoaded.insert(self._randomLine, self._getComment())
			elif self._option == 1:
				self._fileLoaded.insert(self._randomLine, self._getAssignment())
			elif self._option == 2:
				self._fileLoaded.insert(self._randomLine, self._getBoth())
			else:
				print("Invalid option! Terminating...")
				exit(1)
		self._writeFile()


	def __str__(self) -> str:
		'''
		String AbstractFile class method.
		:return: string to print
		'''
		return f"Obfuscate file {self._fileName} with option {self._option} adding {self._lines} lines"
