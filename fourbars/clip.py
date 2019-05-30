import live


class Clip(object):

    set = None
    set = None
    track = None
    clip = None

    def __init__(self):

        self.debug_set_access()
        self.debug_track_access_assume_first_is_midi()
        self.debug_clip_access()

    def debug_set_access(self):
        self.set = live.Set()
        self.set.scan(scan_clip_names = True, scan_devices = True)
        self.set.tempo = 110.0

    def debug_track_access_assume_first_is_midi(self):
        self.track = self.set.tracks[0]
        print("Track name %s" % self.track.name)

    def debug_clip_access(self):
        self.clip = self.track.clips[0]
        print("Clip name %s, length %d beats" % (self.clip.name, self.clip.length))

    def clip_play(self):
        self.clip.play()
