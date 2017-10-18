from gpiozero import PWMLED
from gpiozero.tools import random_values
from signal import pause

"""
random values between 0 and 1 are passed to the LED, giving it a flickering candle effect
"""

led = PWMLED(5)
led.source = random_values()
led.source_delay = 0.1

pause()
