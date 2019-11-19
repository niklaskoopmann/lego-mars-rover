from __future__ import print_function
import pixy
from ctypes import *
from pixy import *

pixy.init ()
pixy.change_prog ("video");

pixy.set_lamp (1, 0);  # switch lamp on on init

# Do magic.

pixy.set_lamp (0, 0);  # switch lamp off on exit