# Author: Andres Tangarife
# Date: 2023-03-01
# Description: Using 0.91" OLED Display with ESP32 to display author's name
#

import ssd1306
from machine import Pin, I2C

# Initialize I2C bus
i2c = I2C(scl=Pin(22), sda=Pin(21))

# Initialize the SSD1306 OLED display with a resolution of 128x32
oled_width = 128
oled_height = 32
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# Clear the display
oled.fill(0)

# Add some text to the display
oled.text("Andres Tangarife", 0, 0)
oled.text("2023-03-01", 0, 10)
oled.show()
