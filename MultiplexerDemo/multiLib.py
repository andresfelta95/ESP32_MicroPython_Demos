#   Class to manage the Multiplexer CD74HC4067 

import machine

class MultiLib:
    def __init__(self, s0, s1, s2, s3, en, signal):
        self.s0 = machine.Pin(s0, machine.Pin.OUT)
        self.s1 = machine.Pin(s1, machine.Pin.OUT)
        self.s2 = machine.Pin(s2, machine.Pin.OUT)
        self.s3 = machine.Pin(s3, machine.Pin.OUT)
        self.en = machine.Pin(en, machine.Pin.OUT)
        self.en.value(1)
        self.signal = machine.ADC(signal)
