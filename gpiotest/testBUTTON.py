from gpiozero import Button

button = Button(16)


#Check if a Button is pressed
while True:
	if button.is_pressed:
		print("Button is pressed")
	else:
		print("Button is not pressed")
	
