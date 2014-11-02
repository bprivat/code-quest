import abc


class CQParser(metaclass=abc.ABCMeta):
    def __init__(self, filename):
        self.set_file(filename)
    
    def set_file(self, filename):
        self._filename = filename
        return self
    
    @staticmethod
    @abc.abstractmethod
    def file_types():
        '''Returns a list of file extensions this Parser can handle'''
        return []
       
    def get_file_content(self):
        '''Given a file name, return the contents of the file as a single string'''
        with open(self._filename) as f:
            return '\n'.join(f.readlines())
        
    @abc.abstractmethod
    def parse_to_xml(self):
        '''Parse associated file and return an XML document as a string'''
        pass
        
    @abc.abstractmethod
    def parse_to_string(self):
        '''Parse associated file and return an XML document as an lxml object'''
        pass