# uncompyle6 version 3.3.3
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.16 (default, Apr 12 2019, 15:32:40) 
# [GCC 4.2.1 Compatible Apple LLVM 10.0.1 (clang-1001.0.46.3)]
# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Push/__init__.py
# Compiled at: 2018-10-05 12:29:56
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.capabilities import controller_id, inport, outport, AUTO_LOAD_KEY, CONTROLLER_ID_KEY, FIRMWARE_KEY, HIDDEN, NOTES_CC, PORTS_KEY, SCRIPT, SYNC, TYPE_KEY
from .firmware_handling import get_provided_firmware_version
from .push import Push

def get_capabilities():
    return {CONTROLLER_ID_KEY: controller_id(vendor_id=2536, product_ids=[
                         21], model_name='Ableton Push'), 
       PORTS_KEY: [
                 inport(props=[HIDDEN, NOTES_CC, SCRIPT]),
                 inport(props=[]),
                 outport(props=[HIDDEN, NOTES_CC, SYNC, SCRIPT]),
                 outport(props=[])], 
       TYPE_KEY: 'push', 
       FIRMWARE_KEY: get_provided_firmware_version(), 
       AUTO_LOAD_KEY: True}


def create_instance(c_instance):
    u""" Creates and returns the Push script """
    return Push(c_instance=c_instance)