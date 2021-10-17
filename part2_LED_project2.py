import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(25, GPIO.IN)

# if button is not pressed light is off, else light is on
# while True:
#     if GPIO.input(25):
#         GPIO.output(18, False)
#     else:
#         GPIO.output(18, True)

pressed = 1

while True:
    if GPIO.input(25):
        GPIO.output(18, False)
    else:
        while (GPIO.input(25)):
            GPIO.output(18, True)
            time.sleep(1)
            GPIO.output(18, False)
            time.sleep(1)
