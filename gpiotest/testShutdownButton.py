from gpiozero import Button
from subprocess import check_call
from signal import pause

"""
The Button class also provides the ability to run a function when the button has been held for a given length of time. This example will shut down the Raspberry Pi when the button is held for 2 seconds:
"""

def shutdown():
	check_call(['sudo','poweroff'])

shutdown_btn = Button(17,hold_time=2)
shutdown_btn.when_held = shutdown

pause()
