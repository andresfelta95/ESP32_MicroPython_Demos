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
#              - S0: Pin 18 (past 4) 
#              - S1: Pin 5 
#              - S2: Pin 17 (past 18)
#              - S3: Pin 16 (past 19)
#              - E: Pin 19 (past 23)
#              The ESP32 is connected to the OLED display as follows:
#              - SDA: Pin 21
#              - SCL: Pin 22
#              - VCC: 3.3V
#              - GND: GND
#              The echo pin of the sensors is connected to the ESP32 as follows:
#              - Sensor 1: Pin 13 (past 32)
#              - Sensor 2: Pin 12 (past 33)
#              - Sensor 3: Pin 14 (past 25)
#              - Sensor 4: Pin 27 (past 26)
#              - Sensor 5: Pin 26 (past 27)
#              - Sensor 6: Pin 25 (past 14)
#              - Sensor 7: Pin 33 (past 12)
#              - Sensor 8: Pin 32 (past 13)
#              - Sensor 9: Pin 35
#              - Sensor 10: Pin 34
#              The trigger pin for the multiplexer is connected to the ESP32 as follows:
#              - Pin 4 (past 15)
# Import the libraries
# from ssd1306 import SSD1306_I2C
from machine import Pin, time_pulse_us
import time
from mux import Mux
import math

# Create the Multiplexer object
mux = Mux(18, 5, 17, 16, 19)

# Create the I2C object
# i2c = I2C(scl=Pin(22), sda=Pin(21))

# Create the OLED object
# oled = SSD1306_I2C(128, 32, i2c)

#Setting the trigger 
trig = Pin(4, Pin.OUT) #was pin 15 

Sound_SPEED = 340
TRIG_PULSE_DURATION_US = 10

# Create the pins for the sensors
sensor1 = Pin(13, Pin.IN)
sensor2 = Pin(12, Pin.IN)
sensor3 = Pin(14, Pin.IN)
sensor4 = Pin(27, Pin.IN)
sensor5 = Pin(26, Pin.IN)
sensor6 = Pin(25, Pin.IN)
sensor7 = Pin(33, Pin.IN)
sensor8 = Pin(32, Pin.IN)
sensor9 = Pin(35, Pin.IN)
sensor10 = Pin(34, Pin.IN)

# Create the list of sensors
sensors = [sensor1, sensor2, sensor3, sensor4, sensor5, sensor6, sensor7, sensor8, sensor9, sensor10]

#points (sending the data one at a time)
player1_points = 0
player2_points = 0

while True:
    # mux.set_channel(0)
    # trig.value(0)
    # time.sleep_us(5)
    # trig.value(1)
    # time.sleep_us(TRIG_PULSE_DURATION_US)
    # trig.value(0)
    # ultrason_duration = time_pulse_us(sensors[0], 1, 30000)
    # print(ultrason_duration)
    # distance_cm = round(Sound_SPEED * ultrason_duration /20000)
    # print(f"Distance Sensor {1} : {distance_cm} cm")
    # if round(distance_cm) == 20 or round(distance_cm) == 19:
    #     print(f'{round(distance_cm)} : bulleye') 
    # time.sleep_ms(500)
    # time.sleep(1)
    
    for i in range(10):
        mux.set_channel(i)
        trig.value(0)
        time.sleep_us(5)
        trig.value(1)
        time.sleep_us(TRIG_PULSE_DURATION_US)
        trig.value(0)
        ultrason_duration = time_pulse_us(sensors[i], 1, 30000)
        distance_cm = Sound_SPEED * ultrason_duration /20000
        print(f"Distance Sensor {i + 1} : {distance_cm} cm")
        time.sleep_ms(500) 
        time.sleep(1)

def findingTheDart(dartList):
    position = 0

    #for dart_pos in dartList:
    
    return position