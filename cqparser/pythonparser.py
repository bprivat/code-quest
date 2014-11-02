import ast

from .cqparser import CQParser


class PythonParser(CQParser):
    def __init__(self, filename):
        super().__init__(filename)

    @staticmethod
    def file_types():
        return ['.py', '.py3']
        
    def parse_to_xml(self):
        content = self.get_file_content()
        
        return ast.parse(content, self._filename)
        
    def parse_to_string(self):
        pass
        
CQParser.register(PythonParser)