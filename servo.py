"""
My own very simple Servo driver object
"""
class Servo:
    
    def __init__ (self, pwm):
        self.pwm = pwm

    """
    Convert 0-180 degrees to the corresponding PWM duty cycle
    and set the duty cycle to move the servo. I experimented
    with the servo to find the actual min/max it would react to
    """

    def _convert(self, x, in_min=0, in_max=180, out_min=1130, out_max=7000):
        # bounds checking
        if in_min < 0:
            in_min = 0
        if in_max > 180:
            in_max = 180

        if x < in_min:
            x = in_min
        if x > in_max:
            x = in_max

        if out_min < 1130:
            out_min = 1130
        if out_max > 7000:
            out_max = 7000

        # do the math ... return the duty cycle as an integer
        return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

    # call the convert function and move the servo
    def set_servo(self, degrees):
        self.pwm.duty_u16(self._convert(degrees))
