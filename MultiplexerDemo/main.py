"""
Authors:                Andres Tangarife & Keven Lou
Date:                   2023-02-14
Description:            Multiplexer Demo to send a a high value to the LED in channels 0 and 14
"""

from machine import Pin
from mux import Mux
import time

# Create the multiplexer object
mux = Mux(13, 12, 14, 27, 26)

#   Create a Signal object in the pin 2
_Signal = Pin(2, Pin.OUT)

#   While loop to send a high value to the LED in channels 0 and 14
while True:
    mux.set_channel(0)
    _Signal.value(1)
    mux.set_channel(14)
    _Signal.value(1)
    time.sleep(1)
