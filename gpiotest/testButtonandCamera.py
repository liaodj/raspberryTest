from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from signal import pause

"""
Using the button press to trigger PiCamera to take a picture using button.when_pressed = camera.capture would not work because the capture() method requires an output parameter. However, this can be achieved using a custom function which requires no parameters:
"""

button = Button(2)
camera = PiCamera()

def capture():
	datetime = datetime.now().isoformat()
	camera.capture('/home/pi/%s.jpg' %datetime)

button.when_pressed = capture

pause()
