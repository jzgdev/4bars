import argparse
import sys
import pkg_resources
from termcolor import colored
from cmd import Cmd


class CommandParser(argparse.ArgumentParser):
    def help_root(self):
        self.desc()
        print("""Usage: 4bars (BETA) [-version] [-help] <command> [args]

The available commands for execution are listed below
Commands marked [WIP] are work-in-progress

Common commands:
    cd          [WIP] essential directory navigation
    set         [WIP] set management
    track       [WIP] current track setup
    device      [WIP] device management
    record      [WIP] record all clips on 4BARS_ prefixed track
    sync        [WIP] synchronize exported assets with 4bars.media
    status      [WIP] check if all requirements and communication is working
    login       [WIP] login to 4bars service. obtain api token""")

    def help_cd(self):
        self.desc()
        print("""Usage: 4bars [-version] [-help] <command> [args]

CD commands are for quick directory navigation. Example: 4bars cd base

cd commands:
    base        4bars base configuration folder
    rec         4bars recordings output folder
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

        description = colored("4bars - (c) 2019 Piotr Styk <dev@4bars.media> - {0}".format(get_version()), 'white', attrs=['bold'])
        print(description)