from gpiozero import LED 
from time import sleep

red = LED(12)

red.on()
sleep(10)
red.off()
sleep(10)
red.on()
sleep(10)
red.off()
sleep(10)

