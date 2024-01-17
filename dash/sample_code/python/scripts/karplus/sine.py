"""
sine.py

Generates a sine wave and saves it n WAVE file format.

Author: Mahesh Venkitachalam
"""

import math
import wave

import numpy as np

sRate = 44100
nSamples = sRate * 5
x = np.arange(nSamples) / float(sRate)
vals = np.sin(2.0 * math.pi * 146.83 * x)
data = np.array(vals * 32767, 'int16').tostring()
file = wave.open('sine146_83.wav', 'wb')
file.setparams((1, 2, sRate, nSamples, 'NONE', 'uncompressed'))
file.writeframes(data)
file.close()
