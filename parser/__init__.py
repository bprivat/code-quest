__all__ = ['pythonparser']

import abc

class Parser(metaclass=abc.ABCMeta):
    @staticmethod
    @abc.abstractmethod
    def file_types():
        '''Returns a list of file extensions this Parser can handle'''
        return []
    
    @staticmethod    
    def getFileContent(filename):
        '''Given a file name, return the contents of the file as a single string'''
        with open(filename) as f:
            return '\n'.join(f.readlines())
        
    @abc.abstractmethod
    def parse(self, filename):
        '''Given a file name, parse it and return an XML document as a string'''
        pass