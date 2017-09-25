from gpiozero import Button
from signal import pause

def say_hello():
	print("Hello!")

button = Button(16)
# Run a function every time the button is pressed:
button.when_pressed = say_hello

pause()

"""
Note that the line button.when_pressed = say_hello does not run the function say_hello, rather it creates a reference to the function to be called when the button is pressed. Accidental use of button.when_pressed = say_hello() would set the when_pressed action to None (the return value of this function) which would mean nothing happens when the button is pressed.
"""
