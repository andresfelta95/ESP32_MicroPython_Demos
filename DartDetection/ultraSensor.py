"""
This module contains the class for the ultrasonic sensor using the HC-SR04 with interrupts and the clock to avoid blocking the main loop
and avoid noise in the readings.
each sensor will have the following attributes:
    * echo - the echo pin of the sensor
    * trig - the trig pin of the sensor (pin 4 for all sensors)
    * location - x, y coordinates of the sensor in cm from the center of the board
    * distance - the distance in cm with 2 decimal places

Author: Andres Tangarife - Keven Lou
Date: 2023-03-17
"""

# Import the libraries
from machine import Pin, time_pulse_us
import time
import math

# Create the class
class UltraSensor:

    #   Initialize the sensor
    def __init__(self, echo, location):
        #   Set the attributes
        self._echo = Pin(echo, Pin.IN)
        self._trig = Pin(4, Pin.OUT)
        self._trig.value(0)
        self._location = location
        self._distance = 0.0
        self._timeOut = 600 #   Timeout in us for the echo pulse
        self._sleep = 0.1 #   Sleep time in s between readings
        self._iterations = 30 #   Number of iterations to get the average distance
        self._perFail = 0.66 #   Percentage of failed readings to consider the sensor as failed


    #   Pulse function to get the echo pulse
    def _pulse(self) -> int:
        #   Send the trig pulse
        tr = self._trig
        tr.value(0)
        time.sleep_us(5)
        tr.value(1)
        time.sleep_us(10)
        tr.value(0)
        #  Try to get the echo pulse
        try:
            return time_pulse_us(self._echo, 1, self._timeOut)
        except OSError as err:
            #   if the e.args[0] == 100 then the echo pulse Timed out
            if e.args[0] == 100:
                raise OSError("Echo pulse timed out")
            raise err
        
    
        
