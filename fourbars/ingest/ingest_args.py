import argparse
from fourbars.core.spawn import Spawn
from fourbars.ingest.ingest import Ingest


class IngestArgs(argparse.ArgumentParser):

    sub_args = None

    def __init__(self, in_sub_args):
        self.sub_args = in_sub_args
        super(IngestArgs, self).__init__()

        self.usage = argparse.SUPPRESS
        self.add_help = False

        # if single (this) subarg, then only help
        if len(self.sub_args) < 2:
            self.help()
            return

        self.add_argument('ingest', help='Subcommand to run')
        self.add_argument('-d', action="store")

        # 1:2 if only one, 1: if more than one expected
        args = self.parse_args(self.sub_args[1:])

        ingest = Ingest(args)

        if not hasattr(ingest, args.ingest):
            self.help()
            exit(1)

        getattr(ingest, args.ingest)()

    # TODO: PLAN (table with processed (not-processed), with bpm calclulated, and confirm on spot plan, transcode, upload
    def help(self):
        Spawn.help_desc()
        print("""Usage: 4bars [-version] [-help] <command> [args]

INGEST commands process, format, catalog 4bars loops. Example: 4bars ingest plan

set commands:
    plan        list duration of each asset, check if each exists (md5) in 4bars online library
                prevents duplication  
    transcode   convert recorded loops (ogg at 320/96kbps)
                high and low quality 
                output json file catalog with details
    share       ingest processed assets into your 4bars account
                future-use-placeholder
    help        this help menu""")
