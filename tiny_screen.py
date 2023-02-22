"""
Demo Three: Tiny Screen
"""
from machine import Pin, I2C
import ssd1306

i2c = I2C(0, scl=Pin(21), sda=Pin(20))

oled = ssd1306.SSD1306_I2C(128, 64, i2c, 60)
oled.fill(0)
oled.text("Hello World",30,30)
oled.show()
