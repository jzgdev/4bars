
import os
import ffmpeg
import hashlib
from enum import Enum
import uuid
from fourbars.core.spawn import Spawn
from fourbars.alive.locations import Locations


class AssetType(Enum):
    AIF_ORG = "aif_org_org"
    OGG_320K = "ogg_320k_libvorbis"
    OGG_96K = "ogg_96k_libvorbis"
    AAC_320K = "aac_320k_aac"
    AAC_96K = "aac_96k_aac"


# Create your dictionary class
class AssetItemDict(dict):

    def add(self, key, value):
        self[key] = value


class Asset(object):

    guid = None
    name = None
    tempo = None
    typ = None
    bars = None
    length = None
    f_owner = None
    f_rythm = None
    f_pitch = None
    f_devices = None
    f_envelope = None
    created = None
    items = AssetItemDict()

    org_abs_path = None
    org_md5 = None
    locations = None

    type_ext = None
    type_bitrate = None
    type_codec = None

    def __init__(self):
        self.locations = Locations()
        pass

    def as_dict(self):
        return {
            'guid': self.guid,
            'items': self.items,
        }

    def __str__(self):
        self.as_dict()

    def type_parser(self, in_asset_type):
        at = in_asset_type.split('_')
        self.type_ext = at[0]
        self.type_bitrate = at[1]
        self.type_codec = at[2]

    def md5(self, fname):
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def get_org_md5(self, in_file_path_full):
        self.org_abs_path = in_file_path_full
        self.org_md5 = self.md5(self.org_abs_path)

    def transcode(self, in_file_path_full):
        self.org_abs_path = in_file_path_full
        self.process_original(AssetType.AIF_ORG)
        self.process_web(AssetType.OGG_320K)
        self.process_web(AssetType.OGG_96K)
        self.process_web(AssetType.AAC_320K)
        self.process_web(AssetType.AAC_96K)
        pass

    def process_original(self, in_asset_type):

        if not self.org_md5:
            self.get_org_md5()

        ai = AssetItem()
        ai.set_new_library_location(in_asset_type,
                                    self.org_abs_path,
                                    self.locations.fourbars_library
                                    )
        # TODO: move mkdir to Spawn
        self.locations.mkdir_p(ai.lib_abs_full_path)
        Spawn.cp(ai.org_abs_path, ai.lib_abs_full_file)
        ai.append_probe(ffmpeg.probe(ai.org_abs_path, cmd='ffprobe'))
        ai.append_md5(self.org_md5)

        self.name = ai.org_name
        self.items.add(AssetType.AIF_ORG, ai)

    # def process_ogg(self, in_asset_type):
    #     ai = AssetItem()
    #     ai.set_new_library_location(in_asset_type,
    #                                 self.org_abs_path,
    #                                 self.locations.fourbars_library
    #                                 )
    #     # TODO: move mkdir to Spawn
    #     self.locations.mkdir_p(ai.lib_abs_full_path)
    #     out, _ = (ffmpeg
    #               .input(ai.org_abs_path)
    #               .output(ai.lib_abs_full_file, progress='-', acodec='libvorbis', **{'b:a': '{0}'.format(in_asset_type.value.split('_')[1])})
    #               .overwrite_output()
    #               .run()
    #               )
    #     ai.append_probe(ffmpeg.probe(ai.lib_abs_full_file, cmd='ffprobe'))
    #     ai.append_md5(self.md5(ai.lib_abs_full_file))
    #
    #     self.name = ai.org_name
    #     self.items.add(in_asset_type, ai)

    def process_web(self, in_asset_type):
        at = in_asset_type.value.split('_')
        type_ext = at[0]
        type_bitrate = at[1]
        type_codec = at[2]

        ai = AssetItem()
        ai.set_new_library_location(in_asset_type,
                                    self.org_abs_path,
                                    self.locations.fourbars_library
                                    )
        # TODO: move mkdir to Spawn
        self.locations.mkdir_p(ai.lib_abs_full_path)
        out, _ = (ffmpeg
                  .input(ai.org_abs_path)
                  .output(ai.lib_abs_full_file, progress='-', acodec='{0}'.format(type_codec), **{'b:a': '{0}'.format(type_bitrate)})
                  .overwrite_output()
                  .run()
                  )
        ai.append_probe(ffmpeg.probe(ai.lib_abs_full_file, cmd='ffprobe'))
        ai.append_md5(self.md5(ai.lib_abs_full_file))

        self.name = ai.org_name
        self.items.add(in_asset_type, ai)


class AssetItem(object):

    guid = None
    codec_name = None
    codec_long_name = None
    codec_type = None
    codec_time_base = None
    sample_fmt = None
    sample_rate = None
    channels = None
    bits_per_sample = None
    time_base = None
    duration_ts = None
    duration = None
    bit_rate = None
    format_name = None
    format_long_name = None
    size = None
    md5 = None
    org_abs_path = None
    org_file = None
    org_ext = None
    org_name = None
    lib_full_path = None
    lib_full_path_encoded = None
    lib_full_file = None
    lib_file = None
    lib_ext = None
    lib_abs_full_path = None
    lib_abs_full_file = None

    def __init__(self):
        pass

    def as_dict(self):
        return {
            'guid': self.guid,
        }

    def __str__(self):
        self.as_dict()

    def set_new_library_location(self, in_asset_type, in_org_full_path, in_fourbars_library):
        self.guid = uuid.uuid4().hex.upper()
        self.org_ext = in_org_full_path.split('.')
        self.org_ext = self.org_ext[len(self.org_ext)-1].lower()
        self.org_abs_path = in_org_full_path
        self.org_file = in_org_full_path.split('/')
        self.org_file = self.org_file[len(self.org_file)-1]
        self.org_name = self.org_file[:len(self.org_file)-len(self.org_ext)-1]
        self.lib_ext = in_asset_type.value.split('_')[0]
        self.lib_full_path = os.path.join(self.guid[:2], self.guid[2:4])
        self.lib_file = "{0}.{1}".format(self.guid, self.lib_ext)
        self.lib_full_file = os.path.join(self.lib_full_path, self.lib_file)
        self.lib_abs_full_path = os.path.join(in_fourbars_library, self.lib_full_path)
        self.lib_abs_full_file = os.path.join(in_fourbars_library, self.lib_full_file)

    def append_probe(self, in_probe):
        self.codec_name = in_probe['streams'][0]['codec_name']
        self.codec_long_name = in_probe['streams'][0]['codec_long_name']
        self.codec_type = in_probe['streams'][0]['codec_type']
        self.codec_time_base = in_probe['streams'][0]['codec_time_base']
        self.sample_fmt = in_probe['streams'][0]['sample_fmt']
        self.sample_rate = in_probe['streams'][0]['sample_rate']
        self.channels = in_probe['streams'][0]['channels']
        self.bits_per_sample = in_probe['streams'][0]['bits_per_sample']
        self.time_base = in_probe['streams'][0]['time_base']
        self.duration_ts = in_probe['streams'][0]['duration_ts']
        self.duration = in_probe['streams'][0]['duration']
        self.bit_rate = in_probe['streams'][0]['bit_rate']
        self.format_name = in_probe['format']['format_name']
        self.format_long_name = in_probe['format']['format_long_name']
        self.size = in_probe['format']['size']

    def append_md5(self, in_md5):
        self.md5 = in_md5

