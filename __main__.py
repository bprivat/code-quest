import argparse
import inspect
import os.path

import cqparser

def _setup_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('command',
                        choices=['validate', 'parse', 'play'],
                        help='Command to execute.')
    parser.add_argument('file',
                        help='The source file to parse. Using the file extension, an applicable CQParser subclass will be looked for in the codequest.cqparser package. If this is a .xml file, it will instead be passed straight to the interpreter.')
    return parser.parse_args()

def _validate(file):
    print("Validate...")

def _parse(file):
    print("Parse...")
    
def _parse_for_play(file):
    ext = os.path.splitext(file)[1]
    if ext == ' ':
        print("Error: Need file extension to determine proper parser.")
        return
    elif ext.lower() == 'xml':
        _play('xml')
    
    parsers = [c[1] for c in inspect.getmembers(cqparser, inspect.isclass) if ext in c[1].file_types()]
    if len(parsers) == 0:
        print("No parsers found for {} files.".format(ext))
    elif len(parsers) == 1:
        print("Parsing {} file with {}...".format(ext, parsers[0].__name__))
        parser = parsers[0](file)
        _play(parser.parse_to_xml())
    else:
        print("Multiple parsers found:\n" + '\n'.join(p.__name__ for p in parsers))

def _play(xml):
    print("XML:", xml)
    

args = _setup_arg_parser()
{'validate': _validate,
 'parse':    _parse,
 'play':     _parse_for_play}[args.command](args.file)