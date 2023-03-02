# Author: Andres Tangarife
# Date: 2023-03-02
# Description: This is a demo to use 10 ultrasonic sensors to detect darts in a
#              dartboard. The sensors are connected to a Multiplexer to reduce
#              the number of pins used in the ESP32.
#              The sensors are connected to the Multiplexer as follows:
#              - Sensor 1: Channel 0
#              - Sensor 2: Channel 1
#              - Sensor 3: Channel 2
#              - Sensor 4: Channel 3
#              - Sensor 5: Channel 4
#              - Sensor 6: Channel 5
#              - Sensor 7: Channel 6
#              - Sensor 8: Channel 7
#              - Sensor 9: Channel 8
#              - Sensor 10: Channel 9
#              The ESP32 is connected to the Multiplexer as follows:
#              - S0: Pin 4
#              - S1: Pin 5
#              - S2: Pin 18
#              - S3: Pin 19
#              - E: Pin 23
#              The ESP32 is connected to the OLED display as follows:
#              - SDA: Pin 21
#              - SCL: Pin 22
#              - VCC: 3.3V
#              - GND: GND
#              The echo pin of the sensors is connected to the ESP32 as follows:
#              - Sensor 1: Pin 32
#              - Sensor 2: Pin 33
#              - Sensor 3: Pin 25
#              - Sensor 4: Pin 26
#              - Sensor 5: Pin 27
#              - Sensor 6: Pin 14
#              - Sensor 7: Pin 12
#              - Sensor 8: Pin 13
#              - Sensor 9: Pin 15
#              - Sensor 10: Pin 2
#              The trigger pin for the multiplexer is connected to the ESP32 as follows:
#              - Pin 4

# Import the libraries
from ssd1306 import SSD1306_I2C
from machine import I2C, Pin
from time import sleep
import mux

# Create the Multiplexer object
mux = mux.Mux(4, 5, 18, 19, 23)

# Create the I2C object
i2c = I2C(scl=Pin(22), sda=Pin(21))

# Create the OLED object
oled = SSD1306_I2C(128, 32, i2c)

# Create the pins for the sensors
sensor1 = Pin(32, Pin.IN)
sensor2 = Pin(33, Pin.IN)
sensor3 = Pin(25, Pin.IN)
sensor4 = Pin(26, Pin.IN)
sensor5 = Pin(27, Pin.IN)
sensor6 = Pin(14, Pin.IN)
sensor7 = Pin(12, Pin.IN)
sensor8 = Pin(13, Pin.IN)
sensor9 = Pin(15, Pin.IN)
sensor10 = Pin(2, Pin.IN)

# Create the list of sensors
sensors = [sensor1, sensor2, sensor3, sensor4, sensor5, sensor6, sensor7, sensor8, sensor9, sensor10]

