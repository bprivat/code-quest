import argparse
import os.path

import cqparser
from game.game_runner import GameRunner
from game.model.dungeon import Dungeon
from game.model.player import Player


def _setup_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('command',
                        choices=['validate', 'parse', 'play'],
                        help='Command to execute.')
    parser.add_argument('file',
                        help='The source file to parse. Using the file extension, an applicable CQParser subclass will '
                             'be looked for in the codequest.cqparser package. If this is a .xml file, it will instead '
                             'be passed straight to the interpreter.')
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
    
    parsers = cqparser.get_parsers_of_type(ext)
    if len(parsers) == 0:
        print("No parsers found for {} files.".format(ext))
    elif len(parsers) == 1:
        parser_name, parser_class = parsers[0]
        print("Parsing {} file with {}...".format(ext, parser_name))
        parser = parser_class(file)
        _play(parser.parse_to_xml())
    else:
        print("Multiple parsers found:\n" + '\n'.join(p.__name__ for p in parsers))


def _play(xml):
    print("XML:", xml)
    GameRunner(Dungeon.from_xml(xml), Player()).run()
    

args = _setup_arg_parser()
{'validate': _validate,
 'parse':    _parse,
 'play':     _parse_for_play}[args.command](args.file)