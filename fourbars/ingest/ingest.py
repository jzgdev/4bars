
from fourbars.ingest.transcode import Transcode


class Ingest(object):

    sub_args = None

    def __init__(self, in_sub_args):
        self.sub_args = in_sub_args

    def transcode(self):
        Transcode(self.sub_args).transcode_folder()

    def share(self):
        print("echo: 4bars ingest process (work in progress)")
        pass