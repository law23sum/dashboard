import radio
from microbit import *

radio.on()
radio.config(power=7, group=1)

while True:
    if button_a.was_pressed():
        radio.send("test")
        display.show(Image.ARROW_N)
        sleep(1000)
        display.clear()
    message = radio.receive()
    if message == 'test':
        display.show(Image.YES)
        sleep(1000)
        display.clear()
