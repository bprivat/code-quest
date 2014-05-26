import abc

class CQParser(metaclass=abc.ABCMeta):
    @staticmethod
    @abc.abstractmethod
    def file_types():
        '''Returns a list of file extensions this Parser can handle'''
        return []
    
    @staticmethod    
    def get_file_content(filename):
        '''Given a file name, return the contents of the file as a single string'''
        with open(filename) as f:
            return '\n'.join(f.readlines())
        
    @abc.abstractmethod
    def parse_to_xml(self, filename):
        '''Given a file name, parse it and return an XML document as a string'''
        pass
        
    @abc.abstractmethod
    def parse_to_string(self, filename):
        '''Given a file name, parse it and return an XML document as an lxml object'''
        pass