# 
# 

import numpy as np
import sounddevice as sd
import random
import time

fs = 44100      # sampling frequency
duration = 0.05  # duration of stimuli (seconds)
standard_freq = 500  # stimuli frequencies
target_freq = 1000

t = np.linspace(0, duration, int(fs * duration), endpoint=False)
standard = np.sin(2*np.pi*standard_freq*t)
target = np.sin(2*np.pi*target_freq*t)

n_trials = 200
target_ratio = 0.20
n_standard = int(n_trials*(1-target_ratio))
n_target = int(n_trials*target_ratio)
trials = ['standard']*n_standard + ['target']*n_target
random.shuffle(trials)

for trial in trials:
    if trial == 'standard':
        sd.play(standard)
    else:
        sd.play(target)

    sd.wait()
    time.sleep(2)