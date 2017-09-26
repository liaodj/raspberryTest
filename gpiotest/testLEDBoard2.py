from gpiozero import LEDBoard
from signal import pause

"""
Using LEDBoard with pwm=True allows each LED’s brightness to be controlled
See more LEDBoard examples in the advanced LEDBoard recipes.
"""

leds = LEDBoard(5,6,13,19,26,pwm=True)

leds.value = (0.2,0.4,0.6,0.8,1.0)

pause()