import numpy as np

sampling_rate = 44100  # Sampling rate for audio (Hz)
duration = 1  # Duration of the waveform (seconds)
t = np.linspace(0, duration, int(duration * sampling_rate))  # Time array

print(t)