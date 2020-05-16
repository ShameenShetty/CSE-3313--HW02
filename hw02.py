"""
2/7/20
@author: Shameen Shetty, 1001429743
"""
import soundfile as sf
import numpy as np


# Line 1 : C,C,G,G,A,A,G,G,F,F,E,E
# Line 2 : D,D,E,C,G,G,F,F,E,E,D,D
# C = 52, D = 54, E = 56, F = 57, G = 59, A = 61

line_one = [52, 52, 59, 59, 61, 61, 59, 59, 57, 57, 56, 56]
line_two = [54, 54, 56, 52, 59, 59, 57, 57, 56, 54, 54, 54]
notes = line_one + line_two

notes = np.repeat(notes, 333)

f = []
for keyNum in notes:
    power = (keyNum - 49)/12
    result = 440 * pow(2, power)
    f.append(result)
    # We are finding the result of f = 400 * 2^((keynumber - 49)/12) for each
    # note, then we append it to f

#Here we use linspace to get 8000 values between 0 and 0.5
t = np.linspace(0.0, 0.5, num=8000)

x = []
for x in range(24*333):
    f_i = f[x]
    t_i = t[x]
    result = np.cos(2 * np.pi * f_i * t_i)
    x.append(result)

samplerate = 8000
sf.write('twinkle.wav', x, samplerate)
