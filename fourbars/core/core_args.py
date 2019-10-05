import argparse
import sys
from fourbars.core.spawn import Spawn
from fourbars.mid.mid_args import MidArgs
from fourbars.alive.alive_args import ALiveArgs


class CoreArgs(argparse.ArgumentParser):

    def __init__(self):
        super(CoreArgs, self).__init__()
        self.usage = argparse.SUPPRESS
        self.add_help = False
        self.add_argument('command')
        args = self.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            self.help()
            exit(1)
        getattr(self, args.command)()

    def mid(self):
        MidArgs(sys.argv[1:])

    def live(self):
        ALiveArgs(sys.argv[1:])

    def log(self):
        Spawn.help_desc()
        Spawn.git_log()

    def update(self):
        Spawn.git_pull()
        Spawn.help_desc()

    def help(self):
        Spawn.help_desc()
        print("""Usage: 4bars [-version] [-help] <command> [args]

The available commands for execution are listed below

Common commands:
    live        Live set management
    mid         operate on MIDI (.mid) files in current directory
    log         show git log of recent commits and comments
    update      update 4bars. git pull of checked out branch    
    """)

    def error(self, message):
        #sys.stderr.write('ERROR: %s\n' % message)
        self.help()
        sys.exit(0)




'''
#    track       [WIP] current track setup
#    device      [WIP] device management
#    record      [WIP] record all clips on 4BARS_ prefixed track
#    sync        [WIP] synchronize exported assets with 4bars.media

#    login       [WIP] login to 4bars service. obtain api token
#    cd          [WIP] essential directory navigation

    @staticmethod
    def help_cd():
        Spawn.help_desc()
        print("""Usage: 4bars [-version] [-help] <command> [args]

CD commands are for quick directory navigation. Example: 4bars cd base

cd commands:
    base            4bars base configuration folder
    prefs           ableton preferences folder
    rec             4bars recordings output folder
    help            this help menu""")

    @staticmethod
    def help_set():
        Spawn.help_desc()
        print("""Usage: 4bars [-version] [-help] <command> [args]

SET commands are for interaction with Live set. Example: 4bars set status

set commands:
    status      get basic info on current set
    help        this help menu""")

    @staticmethod
    def help_get():
        Spawn.help_desc()
        print("""Usage: 4bars [-version] [-help] <command> [args]

GET commands are multilevel element lookups. Example: 4bars get locations

set commands:
    locations      get a list of Ableton and 4bars important folders and files locations
    help           this help menu""")
'''
