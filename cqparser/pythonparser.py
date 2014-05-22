import ast

from .cqparser import CQParser

class PythonParser(CQParser):
    @classmethod
    def file_types(cls):
        return ['.py', '.py3']
        
    def parse(self, filename):
        content = self.getFileContent(filename)
        
        return ast.parse(content, filename)
        
CQParser.register(PythonParser)