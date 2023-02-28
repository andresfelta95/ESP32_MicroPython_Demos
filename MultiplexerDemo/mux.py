#   Class to manage the Multiplexer CD74HC4067 

from machine import Pin, ADC

class Mux:
    
    # Constructor
    def __init__(self, pin_s0, pin_s1, pin_s2, pin_s3, pin_e):
        self.pin_s0 = Pin(pin_s0, Pin.OUT)
        self.pin_s1 = Pin(pin_s1, Pin.OUT)
        self.pin_s2 = Pin(pin_s2, Pin.OUT)
        self.pin_s3 = Pin(pin_s3, Pin.OUT)
        self.pin_e = Pin(pin_e, Pin.OUT)
        self.pin_e.value(1)

    # Set the channel
    def set_channel(self, channel):
        self.pin_s0.value(channel & 0x1)
        self.pin_s1.value(channel & 0x2)
        self.pin_s2.value(channel & 0x4)
        self.pin_s3.value(channel & 0x8)

    """# Read the value of the channel
    def read_channel(self, channel):
        self.set_channel(channel)
        self.pin_e.value(0)
        adc = ADC(0)
        value = adc.read()
        self.pin_e.value(1)
        return value
    """
    