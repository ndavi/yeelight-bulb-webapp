import pyaudio
import numpy as np

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024


maxValue = 2**16
bars = 35
p=pyaudio.PyAudio()
# start Recording
stream = p.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
while True:
    data = np.fromstring(stream.read(1024),dtype=np.int16)
    dataL = data[0::2]
    dataR = data[1::2]
    peakL = np.abs(np.max(dataL)-np.min(dataL))/maxValue
    peakR = np.abs(np.max(dataR)-np.min(dataR))/maxValue
    lString = "#"*int(peakL*bars)+"-"*int(bars-peakL*bars)
    rString = "#"*int(peakR*bars)+"-"*int(bars-peakR*bars)
    print("L=[%s]\tR=[%s]"%(lString, rString))