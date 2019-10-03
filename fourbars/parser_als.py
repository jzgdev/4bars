import xml.etree.ElementTree as ET

# parse track prefixed with "4BARS_"
# if there are more than one, process first found
class ParserAls(object):

    root = None
    track = None

    def __init__(self, als_filename):
        self.root = ET.parse(als_filename).getroot()
        self.get_track_starting_with('4BARS_')

    def get_track_starting_with(self, in_starting_with):
        for audiotrack in self.root.findall('LiveSet/Tracks/AudioTrack'):
            track_name = audiotrack.findall('Name/EffectiveName')[0].get('Value')
            if track_name.startswith(in_starting_with):
                self.track = AlsTrack(audiotrack)
                self.track.name = track_name[len(in_starting_with):]
                pass


class AlsTrack(object):

    name = None
    color_index = None
    track_et = None
    clipslots = []

    def __init__(self, in_track):
        self.track_et = in_track
        self.color_index = self.track_et.findall('ColorIndex')[0].get('Value')
        self.get_clipslots()
        pass

    def get_clipslots (self):
        for clipslot in self.track_et.findall('DeviceChain/MainSequencer/ClipSlotList/ClipSlot'):
            alsslot = AlsClipSlot(clipslot)
            if alsslot.valid:
                self.clipslots.append(alsslot)
        pass


class AlsClipSlot(object):

    clip_et = None
    clip_name = None
    file_name = None
    file_path = ""
    file_abs = None
    valid = False # clip is considered valid if it has an audio file attached (recording)

    def __init__(self, in_clipslot):
        self.clip_et = in_clipslot
        self.get_file_name()
        if not self.valid:
            return # return, not a valid clip
        self.get_clip_name()
        self.get_file_details()

    def get_clip_name(self):
        self.clip_name = self.clip_et.findall('ClipSlot/Value/AudioClip/Name')[0].get('Value')

    def get_file_name(self):
        try:
            self.file_name = self.clip_et.findall('ClipSlot/Value/AudioClip/SampleRef/FileRef/Name')[0].get('Value')
            self.valid = True
        except:
            self.valid = False # for the record



    def get_file_details(self):
        for folder in self.clip_et.findall('ClipSlot/Value/AudioClip/SampleRef/FileRef/SearchHint/PathHint/RelativePathElement'):
            self.file_path = self.file_path + "/" + folder.get('Dir')
        self.file_abs = self.file_path + "/" + self.file_name
        pass
