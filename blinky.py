"""
Demo One: Blinky
"""
from machine import Pin
from time import sleep

# built-in LED
# led = Pin("LED", Pin.OUT)

# led + 100 ohm resistor
led = Pin(16, Pin.OUT)

# turn the LED on and off 10X
for _ in range(1, 10):
    led.on()
    sleep(.5)
    led.off()
    sleep(.5)
