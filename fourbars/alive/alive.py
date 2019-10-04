import argparse
from fourbars.core.parser_cmd import ParserCmd
from fourbars.alive.locations import Locations
from fourbars.alive.import_clip import ImportClip
import os
import sys


class ALive(object):

    parser = None
    subars = None

    def __init__(self, in_subargs):
        self.parser = ParserCmd(
            usage=argparse.SUPPRESS,
            add_help=False)

        self.subargs = in_subargs

        # if single (this) subarg, then only help
        if len(self.subargs) < 2:
            self.parser.help_live()
            return

        self.parser.add_argument('live', help='Subcommand to run')

        args = self.parser.parse_args(in_subargs[1:2])
        if not hasattr(self, args.live):
            self.parser.help_live()
            exit(1)

        # fix to use word import on arg but import is a reserved name
        #if args.live == "import":
        #    args.live = "limport"
        getattr(self, args.live)()

        pass

    def help(self):
        self.parser.help_live()

    def init(self):
        pass

    def up(self):
        pass

    def record(self):
        pass

    def limport(self):
        import_clip = ImportClip()
        import_clip.debug_track_access_assume_first_is_midi()
        import_clip.add_clip()
        import_clip.add_note()

    def locations(self):
        print(Locations().get_fullpretty())
