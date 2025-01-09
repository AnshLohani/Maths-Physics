import numpy as np
import matplotlib.pyplot as plt

#Defined a wave function via numpy
x = 1
wave = np.sin(x)


#Engine Configuration and Design 

ee = bool()
engine_type = str()
cylinders = int()
firing_order = tuple()
force_induction_type = ...

#displacement calculation
'''
bore ---> diameter of the piston
stroke ---> Distance the piston travels in one cycle 
'''
bore = int()
stroke = int()
displacement = np.pi * ((bore/2)**2) * stroke * cylinders

#Variables 
N = 2
'''N---> No. of strokes mostly 2 or 4. Theoretically can be any whole number.'''
rpm = 1000
fundamental_frequency = rpm / 60 / (N/2)

def engine(ee,engine_type,cylinders,firing_order,displacement,force_induction_type,N):
    '''
    engine_type = x
    where x can be one of ["I","V","W","R","F"]
    I ---> Inline 
    R ---> Rotary
    F ---> Flat/Boxer

    restrictions on cylinders:
    1)Possible Engine Configurations 
    2)Hypothetical Engine Configurations

    ee = Binary Possiblity of if the engine exists or possible
    True // False

    firing order - order in which the cylinder fires 
    eg: for an eight cylinder: 1-8-4-3-6-5-7-2

    force_induction_type ---> turbocharged/supercharged/twincharged
    none = 0
    turbocharged = 1
    supercharged = 2
    twincharged = 3
    '''
    ...

sampling_rate = 44100  # Sampling rate for audio (Hz)
duration = 1  # Duration of the waveform (seconds)
t = np.linspace(0, duration, int(duration * sampling_rate))  # Time array

exhaust_wave = np.sin(2 * np.pi * fundamental_frequency * t)

#wave modulation
harmonics = np.zeros_like(t)
for n in range(1, 6):  # First 5 harmonics
    harmonics += np.sin(2 * np.pi * fundamental_frequency * n * t)
exhaust_wave_with_harmonics = exhaust_wave + harmonics
# Plot the waveform
plt.plot(t[:1000], exhaust_wave_with_harmonics[:1000])  # Plot a small portion of the waveform for clarity
plt.title("Engine Exhaust Sound Waveform")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.show()