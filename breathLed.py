import RPi.GPIO
import time
# RPi.GPIO.setmode(RPi.GPIO.BOADR)
# RPi.GPIO.setup(11,RPi.GPIO.OUT)
#
# pwm=RPi.GPIO.PWM(12,50)
# pwm.start(0)

RPi.GPIO.setmode(RPi.GPIO.BOARD)
RPi.GPIO.setup(11,RPi.GPIO.OUT)

pwm=RPi.GPIO.PWM(11,50)
#pwm.start(0)

try:
	while True:
		for i in xrange(0,101,2):
			pwm.ChangeDutyCycle(i)
			time.sleep(.03)
		for i in xrange(100,-1,-2):
			pwm.ChangeDutyCycle(i)
			time.sleep(.03)
except KeyboardInterrupt:
	pass

pwd.stop()

RPi.GPIO.cleanup()
