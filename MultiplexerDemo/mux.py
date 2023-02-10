#   Class to manage the Multiplexer CD74HC4067 

import machine

class Mux:
    
    # Constructor
    def __init__(self, _S0, _S1, _S2, _S3, _EN, _Sig):
        self.S0 = machine.Pin(_S0, machine.Pin.OUT)
        self.S1 = machine.Pin(_S1, machine.Pin.OUT)
        self.S2 = machine.Pin(_S2, machine.Pin.OUT)
        self.S3 = machine.Pin(_S3, machine.Pin.OUT)
        self.EN = machine.Pin(_EN, machine.Pin.OUT)
        self.EN.value(1)
        self.Sig = machine.ADC(machine.Pin(_Sig))

    # Set the channel
    def setChannel(self, _channel):
        self.S0.value((_channel & 0x01) > 0)
        self.S1.value((_channel & 0x02) > 0)
        self.S2.value((_channel & 0x04) > 0)
        self.S3.value((_channel & 0x08) > 0)
        self.EN.value(1)

    