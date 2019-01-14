import signal
import sys
from random import randint

import numpy as np
import pyaudio
from yeelight import *
from time import sleep

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024


def signal_handler(sig, frame):
    bulbs[2].stop_music()
    bulbs[1].stop_music()
    bulbs[20].stop_music()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

bulbs = [Bulb('192.168.1.100'), Bulb('192.168.1.101'), Bulb('192.168.1.102')]

maxValue = 2 ** 16
bars = 35
p = pyaudio.PyAudio()
# start Recording
stream = p.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,
                frames_per_buffer=CHUNK)
bulbs[2].turn_on()
bulbs[2].start_music()

bulbs[1].turn_on()
bulbs[1].start_music()

bulbs[0].turn_on()
bulbs[0].start_music()

bulbs[0].set_brightness(255)
bulbs[1].set_brightness(255)
bulbs[2].set_brightness(255)

i = 0
while True:
    i = i + 1
    data = np.fromstring(stream.read(1024), dtype=np.int16)
    dataL = data[0::2]
    dataR = data[1::2]
    peakL = np.abs(np.max(dataL) - np.min(dataL)) / maxValue
    peakR = np.abs(np.max(dataR) - np.min(dataR)) / maxValue
    lString = "#" * int(peakL * bars) + "-" * int(bars - peakL * bars)
    rString = "#" * int(peakR * bars) + "-" * int(bars - peakR * bars)
    bulbs[0].set_rgb(255, 0, 128)
    bulbs[1].set_rgb(255, 0, 128)
    bulbs[2].set_rgb(255, 0, 128)

    rndm = randint(1, 2)

    if (peakL * 1000 / 2 > 70):
        bulbs[0].set_rgb(0, 255, 0)
        bulbs[1].set_rgb(0, 255, 0)
        bulbs[2].set_rgb(0, 255, 0)
        bulbs[0].set_brightness(peakL * 1000 / 2)
        bulbs[1].set_brightness(peakL * 1000 / 2)
        bulbs[2].set_brightness(peakL * 1000 / 2)
        i = 0
    elif (peakL * 1000 / 2 > 100):

        bulbs[0].set_rgb(255, 255, 255)
        bulbs[1].set_rgb(255, 255, 255)
        bulbs[2].set_rgb(255, 255, 255)

    print(peakL * 1000 / 2)
    #bulbs[0].set_brightness(peakL * 1000 / 2)
    #bulbs[1].set_brightness(peakL * 1000 / 2)
    #bulbs[2].set_brightness(peakL * 1000 / 2)
    i = 0
