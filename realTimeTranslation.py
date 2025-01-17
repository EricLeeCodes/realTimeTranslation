import pyaudio
import numpy as np
import whisper
import wave
import time

p= pyaudio.PyAudio()
frames_per_buffer = 1024

stream = p.open(format=pyaudio.paInt16, # Takes in 16-bit audio
                channels=1, # 1 is mono, 2 is stereo
                rate=16000, 
                input=True,
                input_device_index=1,
                frames_per_buffer=frames_per_buffer)

# Store audio data
frames = []

print("Recording... Press Ctrl + C to stop")

try:
    while True:
        data=stream.read(frames_per_buffer)
        frames.append(data)

# Exits application by Ctrl + C
except KeyboardInterrupt:
    print("\nRecording stopped") 

finally:
    stream.stop_stream()
    stream.close()
    p.terminate()