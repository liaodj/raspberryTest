
from gpiozero import Button
from picamera import PiCamera
from datetime import datetime
from signal import pause


"""
Using the button press to trigger PiCamera to take a picture using button.when_pressed = camera.capture would not work because the capture() method requires an output parameter. However, this can be achieved using a custom function which requires no parameters:
"""

left_button = Button(2)
right_button = Button(3)
camera = PiCamera()

def capture():
	datetime = datetime.now().isoformat()
	camera.capture('/home/pi/%s.jpg' %datetime)

left_button.when_pressed = camera.start_preview
left_button.when_released = camere.stop_preview
right_button.when_pressed = capture

pause()

pause
