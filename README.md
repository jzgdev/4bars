# 4bars by Abletonists
In Ableton Live, automatically record 4 bar sequences. Multi-scene record, then export all new recordings, name them, catalogue them.

## Ableton Workflow as Code
- inject several midi tracks (as code)
- setup devices (as code)
- configure devices (program, controls)
- apply envelopes to clips
- export as 4 bars audio
- use track+clip+RandomName+index naming conventions and output files to destination folder
- (optional) submit 4 bar sequences to 4bars.media for social sequencing

## Requirements
- Ableton Live v10.1+
- python 3.7.2 +
- brew install liblo 
- pylive (freedom to work with Live outside of Live python)
- liveosc (forked for AL10+, comes with pylive)
- ClyphX Pro (commercial version)
- sendmidi receivemidi (for stubborn program changes of vst devices)
- gzip (for extracting of ableton project files)
- Mac OS X (not tested on any other platform at the moment)

## Help
Join "Abletonists" Slack channel. Immediate invitation at: https://abletonists.4bars.media
