"""
Authors:                Andres Tangarife & Keven Lou
Date:                   2023-02-14
Description:            Multiplexer Demo to send a a high value to the LED in channels 0 and 14
"""

from machine import Pin, time_pulse_us
from mux import Mux
import time

# Create the multiplexer object
mux = Mux(13, 12, 14, 27, 26)

#   Create a Signal object in the pin 4
_Signal = Pin(4, Pin.OUT)

# LED pin 2
led = Pin(2, Pin.OUT)

sounn_Speed = 340
TRIG_PULSE_DURATION_US = 10


#   Trig Pins
_Sensor1 = Pin(18, Pin.IN)
_Sensor2 = Pin(33, Pin.IN)
_Sensor3 = Pin(25, Pin.IN)

#   While loop to send a high value to the LED in channels 0 and 14
while True:
    led.value(1)
    print("LED ON")
    mux.set_channel(0)
    _Signal.value(1)
    time.sleep(1)
    led.value(0)
    print("LED OFF")

    mux.set_channel(1)
    _Signal.value(0)
    time.sleep_us(5)
    _Signal.value(1)
    time.sleep_us(TRIG_PULSE_DURATION_US)
    _Signal.value(0)

    ultraSonic_Duration = time_pulse_us(_Sensor1, 1, 30000)
    distance = ultraSonic_Duration * sounn_Speed / 2 / 10000

    print("Distance Sensor #1: ", distance, "cm")
    time.sleep_ms(500)

    mux.set_channel(4)
    _Signal.value(0)
    time.sleep_us(5)
    _Signal.value(1)
    time.sleep_us(TRIG_PULSE_DURATION_US)
    _Signal.value(0)

    ultraSonic_Duration = time_pulse_us(_Sensor2, 1, 30000)
    distance = ultraSonic_Duration * sounn_Speed / 2 / 10000

    print("Distance Sensor #2: ", distance, "cm")
    time.sleep_ms(500)

    mux.set_channel(10)
    _Signal.value(0)
    time.sleep_us(5)
    _Signal.value(1)
    time.sleep_us(TRIG_PULSE_DURATION_US)
    _Signal.value(0)

    ultraSonic_Duration = time_pulse_us(_Sensor3, 1, 30000)
    distance = ultraSonic_Duration * sounn_Speed / 2 / 10000

    print("Distance Sensor #3: ", distance, "cm")
    time.sleep_ms(500)

    mux.set_channel(14)
    _Signal.value(1)
    time.sleep(1)
