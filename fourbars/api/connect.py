import requests
from urllib.parse import urlencode
from collections import OrderedDict
from fourbars.core.settings import Settings


class Connect(object):
    settings = None

    def __init__(self, in_token=None):
        self.settings = Settings()

    def login(self):
        data = OrderedDict([
            ('client_id', self.settings.auth.client),
            ('username', self.settings.auth.username),
            ('password', self.settings.auth.password),
            ('grant_type', 'password')
        ])
        headers={
            'content-type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(self.settings.auth.auth_url,
                                data=urlencode(data),
                                headers=headers
                                )

        self.settings.update_token(response.content)
        pass

    # def get_plain(self):
    #
    #
    # def get(self):
    #     myToken = '<token>'
    #     myUrl = '<website>'
    #     if self.token:
    #         head = {'Authorization': 'token {}'.format(myToken)}
    #     response = requests.get(self.settings.auth.auth_url, headers=head)