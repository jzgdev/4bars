import argparse
import sys
import pkg_resources
from termcolor import colored
from fourbars.core.cmd import Cmd


class ParserCmd(argparse.ArgumentParser):
    def help_root(self):
        self.desc()
        print("""Usage: 4bars [-version] [-help] <command> [args]

The available commands for execution are listed below

Common commands:
    live        Live set management
    mid         operate on MIDI (.mid) files in current directory""")


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
    help        this help menu

optional:
    -d          directory folder""")

    def help_live(self):
        self.desc()
        print("""Usage: 4bars [-version] [-help] <command> [args]

LIVE commands initialize relate to operations on Ableton Live. Example: 4bars live init

set commands:
    init        [WIP] initialize new song/set in current folder
    up          [WIP] start Live and load current project
    import      [WIP] import current folder mid files as clips into current project and track prefixed with 4BARS_
    record      [WIP] record MIDI track prefixed with 4BARS_ and collect recorded assets
    locations   show absolute paths to your Ableton installation
    help        this help menu""")

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
