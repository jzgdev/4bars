import os
import subprocess
import datetime
from termcolor import colored
#import urllib3
#import requests
#import requests.exceptions
import time


class Static(object):


    @staticmethod
    def figlet(msg):
        prov_cmd = "figlet -w 160 {0}".format(msg)
        proc = subprocess.Popen(prov_cmd, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
        out = ''
        for line in iter(proc.stdout.readline, ''):
            out += line
        print(out)

    @staticmethod
    def figletcyber(msg):
        prov_cmd = "figlet -f {0} {1}".format(os.path.join(os.path.dirname(os.path.realpath(__file__)), "cybermedium.flf"), msg)
        proc = subprocess.Popen(prov_cmd, stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
        out = ''
        for line in iter(proc.stdout.readline, ''):
            out += line
        print(out)

    @staticmethod
    def msg(in_service, in_msg):
        print(colored(str(datetime.datetime.now()), 'cyan'), \
              colored(':', 'white'), \
              colored(in_service, 'yellow'), \
              colored('>>', 'white'), \
              colored(in_msg, 'green'))

    @staticmethod
    def msg_bold(in_service, in_msg):
        print(colored(str(datetime.datetime.now()), 'cyan'), \
              colored(':', 'white'), \
              colored(in_service, 'red'), \
              colored('>>', 'white'), \
              colored(in_msg, 'red', attrs=['bold']))

    # TO BE EDITED
    @staticmethod
    def wait_until_url_is_up(self, url, log_msg=None, verify=False, timeout=600, sleep_time=10):
        elapsed_sec = 0
        while True:
            try:
                response = requests.get(url, verify=verify, timeout=timeout)
                response.raise_for_status()
                return True
            except Exception:
                if log_msg:
                    #self.logger.info(log_msg)
                    pass
                elapsed_sec += sleep_time
                if elapsed_sec > timeout:
                    break
                time.sleep(sleep_time)

        return False
