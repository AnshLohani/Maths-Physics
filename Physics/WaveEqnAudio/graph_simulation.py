import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Variables
N = 2  # Number of strokes
sampling_rate = 44100  # Sampling rate for audio (Hz)
duration = 1  # Duration of the waveform (seconds)
t = np.linspace(0, duration, int(duration * sampling_rate))  # Time array

# Function to generate waveform based on RPM
def waveform(rpm):
    fundamental_frequency = rpm / 60 / (N / 2)
    harmonics = np.zeros_like(t)
    
    for n in range(1, 6):  # First 5 harmonics
        harmonics += np.sin(2 * np.pi * fundamental_frequency * n * t)
    
    exhaust_wave = np.sin(2 * np.pi * fundamental_frequency * t)
    exhaust_wave_with_harmonics = exhaust_wave + harmonics
    
    return exhaust_wave_with_harmonics  # Return the complete waveform for the current RPM

# Initialize RPM and the target RPM
rpm = 0
target_rpm = 6000  # Target RPM
acceleration_time = 4  # Time in seconds to go from 0 to target RPM
frame_rate = 30  # Frames per second (30 frames per second)
num_frames = acceleration_time * frame_rate  # Total number of frames (4 seconds * 30 fps)

# RPM increment per frame to reach 6000 RPM in 4 seconds
rpm_increment = target_rpm / num_frames

# Frame rate for animation
frame_interval = 1000 / frame_rate  # Milliseconds between frames

# Create a stream for continuous playback
stream = sd.OutputStream(samplerate=sampling_rate, channels=1, dtype='float32')

# Start the stream
stream.start()

# Function to update the waveform in real-time for animation and audio
def update_waveform(i):
    global rpm

    # Increment RPM per frame
    rpm = rpm + rpm_increment
    if rpm > target_rpm:
        rpm = target_rpm  # Ensure RPM does not exceed the target

    # Generate the waveform for the current RPM
    waveform_data = waveform(rpm)
    if waveform_data is not None:
        # Normalize waveform data to avoid clipping
        waveform_data = waveform_data / np.max(np.abs(waveform_data))  # Normalize
        waveform_data = waveform_data.astype(np.float32)
        
        # Write the waveform data to the stream (this will play the sound)
        stream.write(waveform_data)

    # Visual update for animation
    xaxis = np.linspace(0, rpm, len(waveform_data))
    plt.cla()  # Clear the previous frame
    plt.plot(xaxis, waveform_data)
    plt.title(f"Engine Exhaust Sound Waveform (RPM: {int(rpm)})")
    plt.xlabel("RPM")
    plt.ylabel("Amplitude")

# Create animation for real-time plot updates
ani = FuncAnimation(plt.gcf(), update_waveform, frames=num_frames, interval=frame_interval)

# Show the plot (optional, if you want the waveform to be visualized)
plt.tight_layout()
plt.show()

# Close the stream after the animation is finished (this ensures clean shutdown)
stream.stop()
stream.close()