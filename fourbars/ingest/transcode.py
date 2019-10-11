import os
import ffmpeg
from fourbars.alive.locations import Locations
import hashlib
from fourbars.schema.asset import *

class Transcode(object):

    sub_args = None
    locations = None

    def __init__(self, in_sub_args):
        self.sub_args = in_sub_args
        self.locations = Locations()

    def get_aif_files(self):
        return self.get_files('aif')

    def get_files(self, ext):
        files = [os.path.join(self.locations.pwd, f) for f in os.listdir(self.locations.pwd) if os.path.isfile(os.path.join(self.locations.pwd, f)) and f.lower().endswith(('.{0}'.format(ext)))]
        if len(files) == 0:
            print("No .{0} files".format(ext))
            exit(0)

        return files

    def info(self):

        # if (d)irectory argument specified, overwrite current location
        #getcontext().prec = 6
        #bpm = Decimal(119.00)
        #while bpm <= Decimal(130):
        #    bpm += Decimal(0.01)
        #    beat_sec = Decimal(60) / bpm
        #    fourbars = beat_sec * 4 * 4
        #    #if (fourbars*1000).is_integer():
        #    print (bpm, beat_sec, fourbars)

        if self.sub_args.d:
            self.locations.pwd = self.sub_args.d

        files = self.get_aif_files()
        file_in = files[0]
        asset = Asset()
        asset.transcode(file_in)


        pass

    def md5(self, fname):
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
