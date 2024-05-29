import OPi.GPIO as GPIO

 
try:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    while True:
        GPIO.output(12, GPIO.HIGH)
except KeyboardInterrupt:
    GPIO.cleanup()