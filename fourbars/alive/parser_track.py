import mido
import re
import pretty_midi


class Note(object):
    # PYLIVE EXAMPLE
    # note position duration velocity
    # self.clip.add_note(60, 0, 0.25, 60)
    # self.clip.add_note(60, 1, 0.25, 10)
    # self.clip.add_note(60, 2, 0.25, 120)
    # self.clip.add_note(61, 3, 1, 120)

    note = None
    channel = None
    position = None
    duration = None
    velocity = None
    is_playing = None
    _ticks_start = None
    _ticks_end = None

    def __init__(self, in_note_on, in_clip_cursor):
        self.is_playing = True
        self.note = in_note_on.note
        self.note_pretty = pretty_midi.note_number_to_name(self.note)
        self.velocity = in_note_on.velocity
        self.channel = in_note_on.channel
        self._ticks_start = in_clip_cursor
        pass

    def __str__(self):
        #return 'Note(note={0} velocity={1} ticks_start={2} ticks_end={3} is_playing={4})'.format(self.note_pretty, self.velocity, self._ticks_start, self._ticks_end, self.is_playing)
        return 'Note(note={0} velocity={1} position={2} duration={3})'.format(self.note_pretty, self.velocity, self.position, self.duration)

    def stop(self, in_clip_cursor, in_track_signature):
        self.is_playing = False
        self._ticks_end = in_clip_cursor

        # TODO: not implemented
        self.position = self._ticks_start / in_track_signature.mid_ticks_per_beat
        self.duration = (self._ticks_end - self._ticks_start) / in_track_signature.mid_ticks_per_beat


class Signature(object):

    mid_ticks_per_beat = None
    time_is_default = True
    time_numerator = 4
    time_denominator = 4
    time_clocks_per_click = 96
    time_32nds_per_beat = 8
    time_signature = "4/4"
    time_beat = None
    time_beat_ticks = None
    time_bar = None


    def __init__(self, in_ticks_per_beat):
        self.mid_ticks_per_beat = in_ticks_per_beat
        # 1/32 = 0.03125 (MIDI SPEC DIVIDER)
        self.time_beat = 0.03125 * self.time_32nds_per_beat
        self.time_bar = self.time_numerator * self.time_beat



    def parse_time_signature(self, in_msg):
        self.time_is_default = False
        self.time_numerator = in_msg.numerator
        self.time_denominator = in_msg.denominator
        self.time_clocks_per_click = in_msg.clocks_per_click
        self.time_32nds_per_beat = in_msg.notated_32nd_notes_per_beat
        self.time_signature = "{0}/{1}".format(self.time_numerator, self.time_denominator)

        # 1/32 = 0.03125 (MIDI SPEC DIVIDER)
        self.time_beat = 0.03125 * self.time_32nds_per_beat # = quarternote = 0.25
        self.time_bar_notes = self.time_numerator * self.time_beat
        self.time_bar = self.time_numerator * self.time_beat


class ParserTrack(object):

    mid_track = None
    name = None
    signature = None
    track_string = ""
    clip_notes = []
    clip_cursor = 0

    def __init__(self, in_track, in_ticks_per_beat):
        self.mid_track = in_track
        self.name = self.mid_track.name.rstrip('\x00')
        self.signature = Signature(in_ticks_per_beat)
        self._iterate()

    def __str__(self):
        return self.track_string

    def _iterate(self):
        print()
        for msg in self.mid_track:
            self.clip_cursor += msg.time
            if msg.is_meta and msg.type == 'time_signature':
                self.signature.parse_time_signature(msg)
            elif msg.type.startswith('note_on'):
                # new note append to master index at cursor location
                self.clip_notes.append(Note(msg, self.clip_cursor))
            elif msg.type.startswith('note_off'):
                # ending not currently playing
                # find note, mark end at clip cursor
                for c_note in self.clip_notes:
                    if c_note.note == msg.note:
                        c_note.stop(self.clip_cursor, self.signature)

        self.print_clip_notes()

    def print_clip_notes(self):
        for cn in self.clip_notes:
            self.track_string += "{0}\n".format(cn)
        pass




    #    # translate to pylive compativle
    #    # note position duration velocity
    #    for cn in self.clip_notes:
    #    self.track_string += pretty_midi.note_number_to_name(in_msg.note) + ""
    #    print (in_msg)
    #    return




 #       signature_taken = False
 #   print('Track {}: {}'.format(i, track.name))
 #   for msg in track:
 #       if msg.is_meta and msg.type == 'time_signature' and not signature_taken:
 #           ptrack = ParserTrack()
 #           signature_taken = True
