
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
        file_in = files[0]

        # TODO: Get Asset MD5 and check against API,
        # if not present process
        schema_asset = SchemaAsset()
        schema_asset.get_org_md5(file_in)

        # snd to api get duplicate (hope not)
        #if connect.asset_md5(asset.org_md5):
        #    continue

        schema_asset.transcode(file_in)
        #print(schema_asset.as_json())
        self.api_asset.post(schema_asset)
        pass

