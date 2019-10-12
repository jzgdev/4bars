
from fourbars.schema.asset import *
from fourbars.api.connect import Connect


class Transcode(object):

    sub_args = None
    locations = None

    def __init__(self, in_sub_args):
        self.sub_args = in_sub_args
        self.locations = Locations()

    def transcode_folder(self):

        if self.sub_args.d:
            self.locations.pwd = self.sub_args.d

        files = self.locations.get_aif_files()
        file_in = files[0]
        connect = Connect()
        connect.login()

        asset = Asset()
        asset.get_org_md5(file_in)

        #asset.org_md5


        asset.transcode(file_in)

