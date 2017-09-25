from gpiozero import Button

button = Button(16)

#Wait for a button to be pressed before continuing:
button.wait_for_press()
print("Button was pressed")
