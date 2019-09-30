import argparse
from cmd_parser import CommandParser
import live


class Set(object):

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
            self.parser.help_set()
            return

        self.parser.add_argument('set', help='Subcommand to run')

        args = self.parser.parse_args(in_subargs[1:2])
        if not hasattr(self, args.set):
            self.parser.help_set()
            exit(1)

        getattr(self, args.set)()

        pass

    def get_set_reference(self):
        self.set = live.Set()

    def help(self):
        self.parser.help_set()

    def msg_no_set(self):
        print("STOP: No Live Set Loaded")

    def status(self):
        self.get_set_reference()
        set_open = self.set.currently_open()
        if set_open:
            print("Current Set: {}".format(self.set.currently_open()))
        else:
            self.msg_no_set()

