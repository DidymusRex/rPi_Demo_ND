"""
Demo two: better blinky
"""
from machine import Pin
from neopixel import NeoPixel
from time import sleep, sleep_ms

# set pin 15 to output to drive NeoPixels
pin = Pin(15, Pin.OUT)

# create NeoPixel driver on pin 15 for 17 pixels
np = NeoPixel(pin, 17) 

# a demo I borrowed from Adafruit
def demo(np):
    n = np.n

    # cycle
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (255, 255, 255)
        np.write()
        sleep_ms(25)

    # bounce
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 128)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        sleep_ms(60)

    # fade in/out
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
        np.write()

    # clear
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()

# A demo I asked ChatGPT to write
#   it even comments its code!
def demo_ai(np):
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)] # list of RGB colors to cycle through
    np.fill((0,0,0)) # turn off all pixels to start
    np.write() # update the strip

    # loop through the colors and display each for a short period of time
    for color in colors:
        for i in range(17):
            np[i] = color # set the pixel color
            np.write() # update the strip
            sleep(0.05) # wait a short time before updating the next pixel
            sleep(0.2) # wait a bit longer before moving on to the next color

    # randomly flicker the pixels in a rainbow pattern
    for i in range(100):
        for j in range(17):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            np[j] = (r, g, b) # set a random color
        np.write() # update the strip
        sleep(0.1) # wait a short time before updating the next frame

# Run the demos
demo(np)
demo_ai(np)

# turn off the NeoPixel strip
np.fill((0,0,0))
np.write()
