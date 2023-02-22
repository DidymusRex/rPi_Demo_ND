"""
Demo Four: Move a servo with a knob
"""
from time import sleep
from machine import ADC, Pin, PWM
from servo import Servo

# the potentiometer is on pin 26
pot = ADC(26)

# create a PWM object using pin 14
pwm = PWM(Pin(14))
pwm.freq(50)

# create a servo object using the PWM object
servo = Servo(pwm)

# move the servo to 0 degrees and wait 1 second
servo.set_servo(0)
sleep(1)

# move the servo to 180 degrees and wait 1 second
servo.set_servo(180)
sleep(1)

# an infinite loop that reads the potentiometer then
# converts the ADC value to degrees and moves the servo
while True:
    pot_val = pot.read_u16()

    # avoid divide by zero error
    if pot_val == 0:
        deg = 0
    else:
        deg = pot_val * 180 // 65536

    # print the degrees and move the servo
    print(deg)
    servo.set_servo(deg)

    # a short delay to allow the servo to complete its movement
    sleep(.01)
