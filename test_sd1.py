import numpy as np
import sounddevice as sd

fs = 44100      # sampling frequency
duration = 0.1  # duration of stimuli (seconds)
standard_freq = 500  # stimuli frequencies
target_freq = 1000

t = np.linspace(0, duration, int(fs * duration), endpoint=False)
standard = np.sin(2*np.pi*standard_freq*t)
target = np.sin(2*np.pi*target_freq*t)

sd.play(standard)
sd.play(target)