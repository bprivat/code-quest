import os
import sys
import inspect
import importlib

from .cqparser import CQParser


def is_parser(cls):
    return inspect.isclass(cls) and issubclass(cls, CQParser) and cls is not CQParser


def get_parsers():
    parsers = []
    for root, dirs, files in os.walk(sys.modules[__name__].__path__[0]):
        for file in files:
            if file.endswith('.py') and not file.startswith('__'):
                m_name = file.rstrip('.py')
                m = importlib.import_module(".{}".format(m_name), __name__)
                parsers.extend(inspect.getmembers(m, is_parser))

    return parsers


def get_parsers_of_type(file_type):
    valid_parsers = []
    for p_name, p_class in get_parsers():
        if file_type in p_class.file_types():
            valid_parsers.append((p_name, p_class))

    return valid_parsers