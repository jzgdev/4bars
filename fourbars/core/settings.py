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
        self.auth = Struct(**self.fourbars.auth)
        self.token = Struct(**config_struct.token)
        self.local = Struct(**config_struct.local)
        pass

    def update_token(self, in_content):
        in_content = json.loads(in_content.decode('utf-8'))


        # for line in fileinput.input([self.config_path], inplace=True):
        #     if line.strip().startswith('initial_mass = '):
        #         line = 'initial_mass = 123\n'
        #     sys.stdout.write(line)
        #
        #
        # pysed.
        # pysed.replace(<Old string>, <Replacement String>, <Text File>)
        #

        with open(self.config_path, "r") as sources:
            lines = sources.readlines()
        with open(self.config_path, "w") as sources:
            for line in lines:
                if line.startswith('    access_token'):
                    sources.write('    access_token: "{}"\n'.format(in_content['access_token']))
                elif line.startswith('    expires_in'):
                    sources.write('    expires_in: {}\n'.format(in_content['expires_in']))
                elif line.startswith('    refresh_token'):
                    sources.write('    refresh_token: "{}"\n'.format(in_content['refresh_token']))
                elif line.startswith('    refresh_expires_in'):
                    sources.write('    refresh_expires_in: {}\n'.format(in_content['refresh_expires_in']))
                else:
                    sources.write(line)



        # import warnings
        # warnings.simplefilter('ignore', ruamel.yaml.error.UnsafeLoaderWarning)
        # token = ruamel.yaml.load(open(self.config_path))['token']
        #
        # in_content = json.loads(in_content.decode('utf-8'))
        # token['    access_token'] = in_content['access_token']
        # token['expires_in'] = in_content['expires_in']
        # token['refresh_token'] = in_content['refresh_token']
        # token['refresh_expires_in'] = in_content['refresh_expires_in']
        #
        # with open(self.config_path, 'w') as fp:
        #     yaml.dump(token, fp)


# local:
# library_root: ~/.config/4bars/LIBRARY
# live_root: autodetect
# fourbars:
# auth:
# auth_url: https://id.micromanager.ai/auth/realms/master/protocol/openid-connect/token
# client: ai.micromanager.atos
# username: test01
# password: Password1
# token:
# access_token: a
# expires_in: b
# refresh_token: c
# refresh_expires_in: d

