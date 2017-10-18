import RPi.GPIO as GPIO
import time

PIN_NO = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_NO,GPIO.OUT)

def beep(seconds):
    GPIO.output(PIN_NO,GPIO.HIGH)
    time.sleep(seconds)
    GPIO.output(PIN_NO,GPIO.LOW)
    
def beepAction(secs,sleepsecs,times):
    for i in range(times):
        beep(secs)
        time.sleep(sleepsecs)
        
#beepAction(2,2,2)
GPIO.output(PIN_NO,GPIO.LOW)      
