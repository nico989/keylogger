from abstractFile import AbstractFile


class FilePython(AbstractFile):
	PYTHON_COMMENT_CHARS = ["#", "\"\"\""]


	def __init__(self, fileName: str, option: int, lines: int) -> None:
		'''
		Constructor FilePython class method.
		:return: None
		'''
		super().__init__(fileName, option, lines)


	def _getFileType(self) -> str:
		'''
		Get Python file type.
		:return: Python file type
		'''
		return "py"


	def _getTabs(self, position: int) -> int:
		'''
		Get tabs in Python file.
		:param position: file index
		:return: number of tabs
		'''
		for index in range(position - 1, -1, -1):
			if "def " in self._fileLoaded[index]:
				return 1
			if "\t" in self._fileLoaded[index] and "#" not in self._fileLoaded[index]:
				return self._fileLoaded[index].count("\t")
		return 0
	
	def _getComment(self) -> str:
		'''
		Generate Python random comment.
		:return: Python random comment
		'''
		randomWord = self._generateRandomWord(self.MIN_WORD_LENGTH, self.MAX_WORD_LENGTH)
		if self._getRandomBoolean():
			return f"{self.PYTHON_COMMENT_CHARS[0]}{randomWord}\n"
		else:
			tabs = self._getTabs(self._randomLine)
			return f"\t"*tabs + f"{self.PYTHON_COMMENT_CHARS[1]}\n{randomWord}\n{self.PYTHON_COMMENT_CHARS[1]}\n"

	
	def _getAssignment(self) -> str:
		'''
		Generate Python random assignment.
		:return: Python random assignment
		'''
		randomVariable = self._generateRandomWord(self.MIN_WORD_LENGTH, self.MAX_WORD_LENGTH, 1)
		randomValue = self._generateRandomWord(self.MIN_WORD_LENGTH, self.MAX_WORD_LENGTH)
		tabs = self._getTabs(self._randomLine)
		return f"\t"*tabs + f"{randomVariable} = '{randomValue}'\n"


	def obfuscate(self) -> None:
		'''
		Obfuscate Python input file considering option parameter.
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
		