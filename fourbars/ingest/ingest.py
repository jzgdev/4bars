

from fourbars.ingest.transcode import Transcode
from fourbars.ingest.share import Share


class Ingest(object):

    sub_args = None

    def __init__(self, in_sub_args):
        self.sub_args = in_sub_args

    def transcode(self):
        print("echo: 4bars transcode process (work in progress)")



        transcode = Transcode(self.sub_args).info()
        pass

    def share(self):
        print("echo: 4bars ingest process (work in progress)")
        pass