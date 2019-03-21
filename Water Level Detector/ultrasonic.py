import machine


class Ultrasonic:
    def __init__(self, tPin, ePin):
        # WARNING: Don't use PA4-X5 or PA5-X6 as echo pin without a 1k resistor
        self.triggerPin = tPin
        self.echoPin = ePin

        # Init trigger pin (out)
        self.trigger = machine.Pin(self.triggerPin,machine.Pin.OUT)
        self.trigger.value(0)

        # Init echo pin (in)
        self.echo = machine.Pin(self.echoPin,machine.Pin.IN)

    def distance_in_inches(self):
        return (self.distance_in_cm() * 0.3937)

    def distance_in_cm(self):
        start = 0
        end = 0

        # Send a 10us pulse.
        self.trigger.value(1)
        time.sleep_us(10)
        self.trigger.value(0)

        # Wait 'till whe pulse starts.
        while self.echo.value() == 0:
            pass
        start = time.ticks_us()

        # Wait 'till the pulse is gone.
        while self.echo.value() == 1:
            pass
        end = time.ticks_us()

        # Calc the duration of the recieved pulse, divide the result by
        # 2 (round-trip) and divide it by 29 (the speed of sound is
        # 340 m/s and that is 29 us/cm).
        dist_in_cm = ((end - start) / 2) / 29

        return dist_in_cm
