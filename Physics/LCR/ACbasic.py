import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import datetime  

freq = 50      # Frequency (Hz)
Vo = 1         # Voltage amplitude
Io = 1         # Current amplitude
R = 3          # Resistance

t_window = 0.1          # Length of time window in seconds
fps = 60                # Frames per second
samples_per_frame = 1000

t = np.linspace(0, t_window, samples_per_frame)

fig, ax = plt.subplots()
line_v, = ax.plot(t, np.zeros_like(t), label='Voltage')
line_i, = ax.plot(t, np.zeros_like(t), label='Current', linestyle='--')

ax.set_ylim(-1.5 * max(Vo, Io), 1.5 * max(Vo, Io))
ax.set_xlim(0, t_window)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Amplitude')
ax.set_title('Real-Time Voltage & Current')
ax.legend()
ax.grid(True)

start_time = datetime.datetime.now().timestamp()  # ✅ Use standard datetime

def update(frame):
    current_time = datetime.datetime.now().timestamp() - start_time
    t = np.linspace(current_time, current_time + t_window, samples_per_frame)
    v = Vo * np.sin(2 * np.pi * freq * t)
    i = v / R
    line_v.set_ydata(v)
    line_i.set_ydata(i)
    line_v.set_xdata(t - current_time)
    line_i.set_xdata(t - current_time)
    return line_v, line_i

ani = FuncAnimation(fig, update, interval=300, blit=True)
plt.tight_layout()
plt.show()