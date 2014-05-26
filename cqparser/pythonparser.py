import ast

from .cqparser import CQParser

class PythonParser(CQParser):
    @classmethod
    def file_types(cls):
        return ['.py', '.py3']
        
    def parse_to_xml(self, filename):
        content = self.getFileContent(filename)
        
        return ast.parse(content, filename)
        
    def parse_to_string(self, filename):
        pass
        
CQParser.register(PythonParser)