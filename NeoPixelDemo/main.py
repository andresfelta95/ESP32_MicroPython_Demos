# Demo to show how to use the NeoPixel with the ESP32

from machine import Pin
from neopixel import NeoPixel
import time

# Create a NeoPixel object
np = NeoPixel(Pin(15), 8)


# Function to turn off all the LEDs
def turn_off():
    for i in range(8):
        np[i] = (0, 0, 0)
    np.write()

# Function to turn on all the LEDs with pink color
def turn_on():
    for i in range(8):
        np[i] = (255, 0, 255)
    np.write()

# While loop to turn on and off the LEDs every 1 second
while True:
    turn_on()
    time.sleep(1)
    turn_off()
    time.sleep(1)



