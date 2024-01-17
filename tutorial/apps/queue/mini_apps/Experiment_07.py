import os

from math import sqrt
from microbit import *

filename = 'data.txt'

recording = False
display.show(Image.NO)

while True:
    if button_a.was_pressed():
        recording = not recording
        if recording:
            display.show(Image.YES)
            try:
                os.remove(filename)
            except:
                pass
            fs = open(filename, 'w')
        else:
            display.show(Image.NO)
            fs.close()
    if recording:
        x, y, z = accelerometer.get_values()
        net = sqrt(x * x + y * y + z * z)
        fs.write(str(net))
        fs.write('\n')
        sleep(10)
