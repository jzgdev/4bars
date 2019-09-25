class Cd(object):

    def __init__(self, in_cd):
        if not in_cd:
            self.help()

    def help(self):
        help = """
Usage: 4bars [-version] [-help] <command> [args]

CD commands are for quick directory navigation. Example: 4bars cd base
    base        4bars base folder for projects and recordings
"""


