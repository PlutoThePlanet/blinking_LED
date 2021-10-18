from time import sleep
from gpiozero import LED
from gpiozero import Button

led = LED(18)
button = Button(25)

pressed = False


if button.wait_for_press():
    pressed = True

while pressed:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
    
    if (button.is_pressed):
        pressed = False