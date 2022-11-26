from abstractFile import AbstractFile


class FileCPP(AbstractFile):
	CPP_COMMENT_CHARS = ["//", "/*", "*/"]


	def __init__(self, fileName: str, option: int, lines: int) -> None:
		'''
		Constructor FileCPP class method.
		:return: None
		'''
		super().__init__(fileName, option, lines)


	def _getFileType(self) -> str:
		'''
		Get CPP file type.
		:return: CPP file type
		'''
		return "cpp"
	
	def _getComment(self) -> str:
		'''
		Generate C++ random comment.
		:return: C++ random comment
		'''
		randomWord = self._generateRandomWord(self.MIN_WORD_LENGTH, self.MAX_WORD_LENGTH)
		if self._getRandomBoolean():
			return f"{self.CPP_COMMENT_CHARS[0]}{randomWord}\n"
		else:
			return f"{self.CPP_COMMENT_CHARS[1]}\n{randomWord}\n{self.CPP_COMMENT_CHARS[2]}\n"

	
	def _getAssignment(self) -> str:
		'''
		Generate C++ random assignment.
		:return: C++ random assignment
		'''
		randomVariable = self._generateRandomWord(self.MIN_WORD_LENGTH, self.MAX_WORD_LENGTH, 1)
		randomValue = self._generateRandomWord(self.MIN_WORD_LENGTH, self.MAX_WORD_LENGTH)
		return f"std::string {randomVariable} = \"{randomValue}\";\n"


	def _checkInclude(self) -> bool:
		return "#include <string>\n" in self._fileLoaded
	

	def _getLastInclude(self) -> int:
		for index in range(len(self._fileLoaded) - 1, -1, -1):
			if "#include" in self._fileLoaded[index]:
				return index
		return -1 


	def _fixMain(self) -> None:
		posMain = -1
		for index, line in enumerate(self._fileLoaded):
			if "main" in line:
				posMain = index
			if "{" in line:
				self._fileLoaded.remove(line)
				break
		self._fileLoaded.insert(posMain + 1, "{\n")

	def obfuscate(self) -> None:
		'''
		Obfuscate C++ input file considering option parameter.
		:return: None
		'''
		if not self._checkInclude():
			self._fileLoaded.insert(0, "#include <string>\n")
		
		lineStart = self._getLastInclude() + 1
		
		for _ in range(self._lines):
			self._randomLine = self.getRandomInt(lineStart, len(self._fileLoaded))
			if self._option == 0:
				self._fileLoaded.insert(self._randomLine, self._getComment())
			elif self._option == 1:
				self._fileLoaded.insert(self._randomLine, self._getAssignment())
			elif self._option == 2:
				self._fileLoaded.insert(self._randomLine, self._getBoth())
			else:
				print("Invalid option! Terminating...")
				exit(1)
		self._fixMain()
		self._writeFile()
		