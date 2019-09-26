# uncompyle6 version 3.3.3
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.16 (default, Apr 12 2019, 15:32:40) 
# [GCC 4.2.1 Compatible Apple LLVM 10.0.1 (clang-1001.0.46.3)]
# Embedded file name: /Users/versonator/Jenkins/live/output/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Push/device_component.py
# Compiled at: 2018-11-20 19:30:59
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import liveobj_valid
from ableton.v2.control_surface import ParameterInfo
from ableton.v2.control_surface.components import DeviceComponent as DeviceComponentBase
from ableton.v2.control_surface.control import ButtonControl
from .parameter_mapping_sensitivities import parameter_mapping_sensitivity, fine_grain_parameter_mapping_sensitivity

def is_wavetable(device):
    return liveobj_valid(device) and device.class_name == 'InstrumentVector'


class DeviceComponent(DeviceComponentBase):
    shift_button = ButtonControl()

    @shift_button.pressed
    def shift_button(self, button):
        decorated_device = self.device()
        if is_wavetable(decorated_device):
            decorated_device.osc_1_pitch.adjust_finegrain = True
            decorated_device.osc_2_pitch.adjust_finegrain = True

    @shift_button.released
    def shift_button(self, button):
        decorated_device = self.device()
        if is_wavetable(decorated_device):
            decorated_device.osc_1_pitch.adjust_finegrain = False
            decorated_device.osc_2_pitch.adjust_finegrain = False

    def _create_parameter_info(self, parameter, name):
        device_class_name = self.device().class_name
        return ParameterInfo(parameter=parameter, name=name, default_encoder_sensitivity=parameter_mapping_sensitivity(parameter, device_class_name), fine_grain_encoder_sensitivity=fine_grain_parameter_mapping_sensitivity(parameter, device_class_name))