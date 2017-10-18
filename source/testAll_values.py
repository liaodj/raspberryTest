from gpiozero import Button, LED
from gpiozero.tools import all_values
from signal import pause

button_a = Button(16)
button_b = Button(21)
led = LED(19)

led.source = all_values(button_a.values, button_b.values)

pause()
