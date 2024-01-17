from math import sqrt
from microbit import *

while True:
    x, y, z = accelerometer.get_values()
    net = sqrt(x * x + y * y + z * z)
    print((net,))
    sleep(100)
