from time import sleep
from machine import Pin, PWM
from servo import Servo

pwm = PWM(Pin(14))
pwm.freq(50)

servo = Servo(pwm)

servo.set_servo(0)
sleep(1)

servo.set_servo(180)
