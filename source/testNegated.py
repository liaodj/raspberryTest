from gpiozero import Button,LED
from gpiozero.tools import negated
from signal import pause

"""
In this example, the LED is lit only when the button is not pressed
"""

led = LED(13)
btn = Button(16)

led.source = negated(btn.values)

pause()
