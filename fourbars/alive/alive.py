
from fourbars.alive.locations import Locations
from fourbars.alive.import_clip import ImportClip


class ALive(object):

    sub_args = None

    def __init__(self, in_sub_args):
        self.sub_args = in_sub_args

    def init(self):
        pass

    def up(self):
        pass

    def record(self):
        pass

    def limport(self):
        import_clip = ImportClip()
        import_clip.debug_track_access_assume_first_is_midi()
        import_clip.add_clip()
        import_clip.add_note()

    def locations(self):
        print(Locations().get_fullpretty())
