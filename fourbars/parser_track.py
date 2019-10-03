import mido
import re
import pretty_midi

class ParserTrack(object):

    mid_track = None
    name = None
    time_is_default = True
    time_numerator = 4
    time_denominator = 4
    time_clocks_per_click = 96
    time_32nds_per_quarternote = 8
    time_signature = "4/4"
    track_string = ""

    def __init__(self, in_track):
        self.mid_track = in_track
        self.name = self.mid_track.name.rstrip('\x00')

        self._iterate()

        pass

    def _iterate(self):
        print()
        for msg in self.mid_track:
            if msg.is_meta and msg.type == 'time_signature':
                self._parse_time_signature(msg)
            elif msg.type == 'note_on':
                self._parse_notes(msg)
            elif msg.type == 'note_off':
                self._parse_notes(msg)


    def _parse_time_signature(self, in_msg):
        self.time_is_default = False
        self.time_numerator = in_msg.numerator
        self.time_denominator = in_msg.denominator
        self.time_clocks_per_click = in_msg.clocks_per_click
        self.time_32nds_per_quarternote = in_msg.notated_32nd_notes_per_beat
        self.time_signature = "{0}/{1}".format(self.time_numerator, self.time_denominator)

    def _parse_notes(self, in_msg):
        # translate to pylive compativle
        # note position duration velocity
        self.track_string += pretty_midi.note_number_to_name(in_msg.note) + ""
        #print (in_msg)
        return




 #       signature_taken = False
 #   print('Track {}: {}'.format(i, track.name))
 #   for msg in track:
 #       if msg.is_meta and msg.type == 'time_signature' and not signature_taken:
 #           ptrack = ParserTrack()
 #           signature_taken = True