from abstractFile import AbstractFile


class FilePython(AbstractFile):
    PYTHON_COMMENT_CHARS = ["#", "\"\"\"", "\"\"\""]


    def __init__(self, fileName: str, option: int, lines: int) -> None:
        '''
		Constructor FilePython class method.
		:return: None
		'''
        super().__init__(fileName, option, lines)


    def _getFileType(self) -> str:
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
            return f"\t"*tabs + f"{self.PYTHON_COMMENT_CHARS[1]}\n{randomWord}\n{self.PYTHON_COMMENT_CHARS[2]}\n"

    
    def _getAssignment(self) -> str:
        '''
		Generate Python random assignment.
		:return: Python random assignment
		'''
        randomVariable = self._generateRandomWord(self.MIN_WORD_LENGTH, self.MAX_WORD_LENGTH, 1)
        randomValue = self._generateRandomWord(self.MIN_WORD_LENGTH, self.MAX_WORD_LENGTH)
        tabs = self._getTabs(self._randomLine)
        return f"\t"*tabs + f"{randomVariable} = '{randomValue}'\n"
