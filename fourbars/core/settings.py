#!/usr/bin/env python
"""
MIT License

Copyright (c) 2019 Piotr Styk <polfilm@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""



import yamlordereddictloader
import os
import yaml
from os.path import expanduser
import os.path
import sys
import fileinput
import json
from datetime import datetime, timezone, timedelta
import rfc3339      # for date object -> date string
import iso8601      # for date string -> date object


class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)

    def __getitem__(self, val):
        print(val)


class Settings(object):
    config_path = None
    fourbars = None
    auth = None
    token = None
    local = None
    api = None

    def __init__(self):
        self.config_path = expanduser('~/.config/4bars/4bars.yaml')
        self.load_configfile()

    def load_configfile(self):
        config_data = None
        if os.path.isfile(self.config_path):
            config_data = yaml.load(open(self.config_path), Loader=yamlordereddictloader.Loader)
        else:
            print("4bars.yaml not found in ~/.config/4bars/")
            raise SystemExit(12)

        config_struct = Struct(**config_data)
        self.fourbars = Struct(**config_struct.fourbars)
        self.api = self.fourbars.api
        self.auth = Struct(**self.fourbars.auth)
        self.token = Struct(**config_struct.token)
        self.local = Struct(**config_struct.local)
        pass

    def get_atoken_rtoken_seconds_to_expiry(self):
        atoken = self.get_date_from_str(self.token.expires_after)
        atoken_diff = atoken - self.get_now_local()

        rtoken = self.get_date_from_str(self.token.refresh_expires_after)
        rtoken_diff = rtoken - self.get_now_local()
        return atoken_diff.total_seconds(), rtoken_diff.total_seconds()

    def get_timezone_local_as_str(self):
        return str(datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo)

    def get_now_local_as_str(self, add_seconds=0):
        if add_seconds > 0:
            return self.get_str_from_date(datetime.now(timezone.utc).astimezone() + timedelta(seconds=add_seconds))
        else:
            return self.get_str_from_date(datetime.now(timezone.utc).astimezone())

    def get_now_local(self, add_seconds=0):
        if add_seconds > 0:
            return datetime.now(timezone.utc).astimezone() + timedelta(seconds=add_seconds)
        else:
            return datetime.now(timezone.utc).astimezone()

    def get_date_from_str(self, date_string):
        return iso8601.parse_date(date_string)

    def get_str_from_date(self, date_object):
        return rfc3339.rfc3339(date_object)

    def update_token(self, in_content):
        in_content = json.loads(in_content.decode('utf-8'))

        with open(self.config_path, "r") as sources:
            lines = sources.readlines()
        with open(self.config_path, "w") as sources:
            for line in lines:
                if line.startswith('    access_token'):
                    sources.write('    access_token: "{}"\n'.format(in_content['access_token']))
                elif line.startswith('    expires_in'):
                    sources.write('    expires_in: {}\n'.format(in_content['expires_in']))
                elif line.startswith('    expires_after'):
                    b = self.get_now_local_as_str(int(in_content['expires_in']))
                    sources.write('    expires_after: "{}"\n'.format(b))
                elif line.startswith('    refresh_token'):
                    sources.write('    refresh_token: "{}"\n'.format(in_content['refresh_token']))
                elif line.startswith('    refresh_expires_in'):
                    sources.write('    refresh_expires_in: {}\n'.format(in_content['refresh_expires_in']))
                elif line.startswith('    refresh_expires_after'):
                    b = self.get_now_local_as_str(int(in_content['refresh_expires_in']))
                    sources.write('    refresh_expires_after: "{}"\n'.format(b))
                else:
                    sources.write(line)


    def init_configfile(self):
        # TODO: for now reference below ( ~/.config/4bars/4bars.yaml )
        # local:
        #     library_root: ~/.config/4bars/LIBRARY
        #     live_root: autodetect
        # fourbars:
        #     auth:
        #         auth_url: https://id.micromanager.ai/auth/realms/master/protocol/openid-connect/token
        #         client: ai.micromanager.atos
        #         username: <user>
        #         password: <password>
        # token:
        #     access_token: "<atoken>"
        #     expires_in: 7200
        #     refresh_token: "<rtoken>"
        #     refresh_expires_in: 1800
        pass

