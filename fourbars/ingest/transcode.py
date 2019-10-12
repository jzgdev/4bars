
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

        connect = Connect()
        if not connect.login():
            print ("Login Failed")
            return

        # TODO: iterate through all - 0 is for testing now
        files = self.locations.get_aif_files()
        file_in = files[0]

        # TODO: Get Asset MD5 and check against API,
        # if not present process
        asset = Asset()
        asset.get_org_md5(file_in)

        # snd to api get duplicate (hope not)
        #asset.org_md5


        asset.transcode(file_in)

