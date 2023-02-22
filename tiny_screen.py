"""
Demo Three: Tiny Screen
"""
from machine import Pin, I2C
import ssd1306

# create the I2C object
i2c = I2C(0, scl=Pin(21), sda=Pin(20))

# create the OLED object attached to the I2C bus
oled = ssd1306.SSD1306_I2C(128, 64, i2c, 60)

# set all the pixels to black
oled.fill(0)

# display some text
oled.text("Hello World",1,10)

# update the display from the buffer
oled.show()
