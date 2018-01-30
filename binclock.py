import time
from gpiozero import LED

class BinaryClock(object):
    """ Binary Clock for the Raspberry Pi
        Connect the LEDs to the GPIO as follows:
        Hours - 4 LEDs: GP17-GP16-GP15-GP14
        Minutes - 6 LEDs: GP13-GP12-GP11-GP10-GP9-GP8
        Seconds - 6 LEDs: GP7-GP6-GP5-GP4-GP3-GP2
        The hour is in 12h mode.
        Example:
            1100 : 100110 : 001011 -> 12:38:11 """
    
    # Change the tuples below to use different GPIO pins
    led_hours = LED(14), LED(15), LED(16), LED(17)
    led_mins = LED(8), LED(9), LED(10), LED(11), LED(12), LED(13) 
    led_secs = LED(2), LED(3), LED(4), LED(5), LED(6), LED(7) 

    def __init__(self):
        """ Initialiaze the timer handlers """
        pass

    def start(self):
        """ Start the timer """
        self._update_time()

    def _update_time(self):
        """ Read the time and update the display """
        while True:
            self._update_display(time.localtime())
            time.sleep(1.0 - time.time() % 1.0)

    def _update_display(self, currenttime):
        """ Update the GPIO pins """

        # Hours
        for i in range(4):
            if (currenttime[3] % 12) & (0x01 << i):
                self.led_hours[i].on()
            else:
                self.led_hours[i].off()
        
        # Minutes
        for i in range(6):
            if currenttime[4] & (0x01 << i):
                self.led_mins[i].on()
            else:
                self.led_mins[i].off()
        
        # Seconds
        for i in range(6):
            if currenttime[5] & (0x01 << i):
                self.led_secs[i].on()
            else:
                self.led_secs[i].off()

def main():
    # Get the handler bot
    clock = BinaryClock()
    clock.start()


if __name__ == '__main__':
    main()
