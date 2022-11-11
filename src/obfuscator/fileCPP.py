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
        return f"string {randomVariable} = '{randomValue}';\n"
