import argparse

parser = argparse.ArgumentParser()
parser.add_argument('source_file', 
                    help='The source file to parse. Using the file extension, an applicable Parser class will be looked for in the codequest.parser package. If this is a .xml file, it will instead be passed straight to the interpreter')
                    
