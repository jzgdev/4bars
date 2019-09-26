import argparse
from cmd_parser import CommandParser


class Cd(object):

    parser = None
    subars = None

    def __init__(self, in_subargs):
        self.parser = CommandParser(
            usage=argparse.SUPPRESS,
            add_help=False)

        self.subargs = in_subargs

        # if single (this) subarg, then only help
        if len(self.subargs) < 2:
            self.parser.help_cd()
            return

        self.parser.add_argument('cd', help='Subcommand to run')

        args = self.parser.parse_args(in_subargs[1:2])
        if not hasattr(self, args.cd):
            self.parser.help_cd()
            exit(1)

        getattr(self, args.cd)()

        pass

    def help(self):
        self.parser.help_cd()

    def rec(self):
        print("REC")

