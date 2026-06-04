import numpy as np
import random

n_trials = 200
ratio_oddball = 0.2
trials = np.zeros(n_trials)
idx_odd = np.sort(np.array(random.sample(range(0, n_trials), int(n_trials * ratio_oddball))))
while any(np.diff(idx_odd) <= 1) or idx_odd[0] < 4:
    idx_odd = np.sort(np.array(random.sample(range(0, n_trials), int(n_trials * ratio_oddball))))

trials[np.array(idx_odd)] = 1

print(trials)