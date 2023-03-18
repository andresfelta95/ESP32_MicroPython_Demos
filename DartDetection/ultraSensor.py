"""
This module contains the class for the ultrasonic sensor using the HC-SR04 with interrupts and the clock to avoid blocking the main loop
and avoid noise in the readings
Author: Andres Tangarife - Keven Lou
Date: 2023-03-17
"""

# Import the libraries
from machine import Pin, time_pulse_us
import time
import math

# Create the class
class UltraSensor:

    # Create the constructor
    def __init__(self, echo, trig, mux, mux_channel, name):
        # Create the attributes
        self.echo = echo
        self.trig = trig
        self.mux = mux
        self.mux_channel = mux_channel
        self.name = name
        self.distance = 0
        self.time = 0
        self.sound_speed = 340

        # Create the interrupt
        self.echo.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=self._echo_handler)

    # Create the method to read the distance
    def read_distance(self):
        # Set the trigger to high
        self.trig.value(1)
        # Wait 10 microseconds
        time.sleep_us(10)
        # Set the trigger to low
        self.trig.value(0)
        # Wait for the echo to go high
        while self.echo.value() == 0:
            pass
        # Get the time when the echo goes high
        t1 = time.ticks_us()
        # Wait for the echo to go low
        while self.echo.value() == 1:
            pass
        # Get the time when the echo goes low
        t2 = time.ticks_us()
        # Calculate the time difference
        self.time = time.ticks_diff(t2, t1)
        # Calculate the distance
        self.distance = self.time * self.sound_speed / 2 / 1000000

    # Create the method to read the distance
    def read_distance_mux(self):
        # Set the trigger to high
        self.trig.value(1)
        # Wait 10 microseconds
        time.sleep_us(10)
        # Set the trigger to low
        self.trig.value(0)
        # Wait for the echo to go high
        while self.echo.value() == 0:
            pass
        # Get the time when the echo goes high
        t1 = time.ticks_us()
        # Wait for the echo to go low
        while self.echo.value() == 1:
            pass
        # Get the time when the echo goes low
        t2 = time.ticks_us()
        # Calculate the time difference
        self.time = time.ticks_diff(t2, t1)
        # Calculate the distance
        self.distance = self.time * self.sound_speed / 2 / 1000000
        
