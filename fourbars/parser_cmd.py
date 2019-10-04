import argparse
import sys
import pkg_resources
from termcolor import colored
from cmd import Cmd


class ParserCmd(argparse.ArgumentParser):
    def help_root(self):
        self.desc()
        print("""Usage: 4bars [-version] [-help] <command> [args]

The available commands for execution are listed below
Commands marked [WIP] are work-in-progress

Common commands:
    init        initialize new 4bars project
    set         Live set management
    get         multilevel configuration lookup
    mid         operate on MIDI (.mid) files in current directory
    status      update on status of installation""")


#    track       [WIP] current track setup
#    device      [WIP] device management
#    record      [WIP] record all clips on 4BARS_ prefixed track
#    sync        [WIP] synchronize exported assets with 4bars.media

#    login       [WIP] login to 4bars service. obtain api token
#    cd          [WIP] essential directory navigation

    def help_cd(self):
        self.desc()
        print("""Usage: 4bars [-version] [-help] <command> [args]

CD commands are for quick directory navigation. Example: 4bars cd base

cd commands:
    base            4bars base configuration folder
    prefs           ableton preferences folder
    rec             4bars recordings output folder
    help            this help menu""")

    def help_set(self):
        self.desc()
        print("""Usage: 4bars [-version] [-help] <command> [args]

SET commands are for interaction with Live set. Example: 4bars set status

set commands:
    status      get basic info on current set
    help        this help menu""")

    def help_get(self):
        self.desc()
        print("""Usage: 4bars [-version] [-help] <command> [args]

GET commands are multilevel element lookups. Example: 4bars get locations

set commands:
    locations      get a list of Ableton and 4bars important folders and files locations
    help           this help menu""")

    def help_mid(self):
        self.desc()
        print("""Usage: 4bars [-version] [-help] <command> [args]

MID commands operate on MIDI (.mid) files current or specified (-d) directory. Example: 4bars mid notes

mid commands:
    tracks      list tracks of all midi-based files in current directory
    notes       list notes in tracks using 4bars notation
    push        push mid files into Live clips on a single track prefixed with 4BARS_
    help        this help menu

optional:
    -d          directory folder""")

    def help_init(self):
        self.desc()
        print("""Usage: 4bars [-version] [-help] <command> [args]

INIT commands initialize current folder with 4bars Live set. Example: 4bars init

set commands:
    help           this help menu""")

    def error(self, message):
        #sys.stderr.write('ERROR: %s\n' % message)
        self.help_root()
        sys.exit(0)

    def desc(self):

        def get_version():
            try:
                return pkg_resources.get_distribution("4bars").version
            except:
                return Cmd.local_run_get_out("get version", "git describe --tags")

        description = colored("4bars (BETA) (c) 2019 Piotr Styk <dev@4bars.media> {0}".format(get_version()), 'white', attrs=['bold'])
        print(description)