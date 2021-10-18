import RPi.GPIO as GPIO
import time
from gpiozero import LED
from gpiozero import Button

led = LED(18)
button = Button(25)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN)

pressed = 0

while True:
    button.wait_for_press()
    pressed += 1
    
    while (pressed % 2 == 0):
        GPIO.output(led, True)
        time.sleep(1)
        GPIO.output(button, False)
        time.sleep(1)
        if button.wait_for_press():
            break
    else:
        GPIO.output(led, False)