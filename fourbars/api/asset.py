import requests
from urllib.parse import urlencode
from collections import OrderedDict
from fourbars.api.connect import Connect
import json

class Asset(object):
    connect = None

    def __init__(self):
        self.connect = Connect()
        if not self.connect.login():
            print("Login Failed")
            return

    def post(self, in_schema_asset):

        headers = {
            'Authorization': '{0}'.format(self.connect.get_auth_header()),
            'content-type': 'application/json'
        }
        response = requests.post(self.connect.settings.api+'asset/',
                                 json=json.dumps(in_schema_asset.as_json()),
                                 headers=headers
                                 )

        print()
        print(response.status_code, response.text)
        pass
    # /asset/md5/quick/<md5>
    # return empty 200 if nothing
    # return asset item guid if found 200
