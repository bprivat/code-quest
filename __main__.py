import argparse
import inspect
import os.path

import cqparser

parser = argparse.ArgumentParser()
parser.add_argument('source_file',
                    help='The source file to parse. Using the file extension, an applicable CQParser subclass will be looked for in the codequest.cqparser package. If this is a .xml file, it will instead be passed straight to the interpreter.')
                    
args = parser.parse_args()
ext = os.path.splitext(args.source_file)[1]

if ext.lower() == '.xml':
    print("Interpreting XML file...")
else:
    parsers = [c[1] for c in inspect.getmembers(cqparser, inspect.isclass) if ext in c[1].file_types()]
    if len(parsers) == 0:
        print("No parsers found for {} files.".format(ext))
    elif len(parsers) == 1:
        print("Parsing {} file with {}...".format(ext, parsers[0].__name__))
    else:
        print("Multiple parsers found:\n" + '\n'.join(p.__name__ for p in parsers))