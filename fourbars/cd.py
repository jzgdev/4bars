import argparse
from cmd_parser import CommandParser


class Cd(object):

    parser = None

    def __init__(self, in_subarg):
        self.parser = CommandParser(
            usage=argparse.SUPPRESS,
            add_help=False)

        self.parser.add_argument('cd', help='Subcommand to run')

        args = self.parser.parse_args(in_subarg[1:2])
        if not hasattr(self, args.cd):
            self.parser.help_cd()
            exit(1)

        getattr(self, args.cd)()

        pass

    def help(self):
        self.parser.help_cd()

    def rec(self):
        print("REC")

