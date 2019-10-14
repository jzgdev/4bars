
from fourbars.schema.asset import Asset as SchemaAsset
from fourbars.api.asset import Asset as ApiAsset
from fourbars.alive.locations import Locations

class Transcode(object):

    sub_args = None
    locations = None
    api_asset = None

    def __init__(self, in_sub_args):
        self.sub_args = in_sub_args
        self.locations = Locations()
        self.api_asset = ApiAsset()

    def transcode_folder(self):

        if self.sub_args.d:
            self.locations.pwd = self.sub_args.d

        # TODO: iterate through all - 0 is for testing now
        files = self.locations.get_aif_files()

        for file in files:
            # obtain md5 of file to be submitted
            schema_asset = SchemaAsset()
            schema_asset.get_org_md5(file)

            # check if md5 of file to be submitted exists in 4bars database
            existing_guid = self.api_asset.get_md5_quick(schema_asset.org_md5)
            if existing_guid:
                # item abort, already exists in 4bars database
                print("Skipping ORG: {0}".format(existing_guid))
                continue
            else:
                print("Processing: {0}".format(file))

            # transcode original asset
            schema_asset.transcode(file)

            # post all transcoded assets and link with original
            self.api_asset.post(schema_asset)
