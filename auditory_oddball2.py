from psychopy import prefs
# select PTB
prefs.hardware['audioLib'] = ['ptb']
from psychopy import sound, core
from sound import fetch_sound
import numpy as np
import random

freq_standard = 500 # standard freqency
freq_target = 1000  # target frequency

standard = sound.Sound(fetch_sound(freq_standard))
target = sound.Sound(fetch_sound(freq_target))

n_trials = 200
ratio_oddball = 0.2
trials = np.zeros(n_trials)
idx_odd = np.sort(np.array(random.sample(range(0, n_trials), int(n_trials * ratio_oddball))))
while any(np.diff(idx_odd) <= 1) or idx_odd[0] < 4:
    idx_odd = np.sort(np.array(random.sample(range(0, n_trials), int(n_trials * ratio_oddball))))

trials[np.array(idx_odd)] = 1

isi_list = np.random.uniform(2.0, 3.0, n_trials)

core.wait(2)
for trial, isi in zip(trials, isi_list):
    if trial == 0:
        standard.play()
        print(0)
    else:
        target.play()
        print(1)
    core.wait(isi)
core.wait(2)