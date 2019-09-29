import argparse
from cmd_parser import CommandParser
import live
from locations import Locations

class Get(object):

    parser = None
    subars = None
    set = None

    def __init__(self, in_subargs):
        self.parser = CommandParser(
            usage=argparse.SUPPRESS,
            add_help=False)

        self.subargs = in_subargs

        # if single (this) subarg, then only help
        if len(self.subargs) < 2:
            self.parser.help_get()
            return

        self.parser.add_argument('get')

        args = self.parser.parse_args(in_subargs[1:2])
        if not hasattr(self, args.get):
            self.parser.help_get()
            exit(1)

        getattr(self, args.get)()

        pass

    def locations(self):
        print(Locations().get_fullpretty())

    def help(self):
        self.parser.help_set()


