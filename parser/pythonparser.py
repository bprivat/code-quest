import ast
from . import Parser

class PythonParser(Parser):
    @classmethod
    def file_types(cls):
        return ['.py', '.py3']
        
    def parse(self, filename):
        content = self.getFileContent(filename)
        
        return ast.parse(content, filename)