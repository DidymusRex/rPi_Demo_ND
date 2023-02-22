class Servo:
    
    def __init__ (self, pwm):
            self.pwm = pwm

    def _convert(self, x, in_min=0, in_max=180, out_min=1130, out_max=7000):
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

        return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

    def set_servo(self, degrees):
        self.pwm.duty_u16(self._convert(degrees))
