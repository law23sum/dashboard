import music
from microbit import *

while True:
    if compass.get_field_strength() < 160000:
        music.pitch(523, 1000)
