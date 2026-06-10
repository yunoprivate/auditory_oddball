# utils.py
import numpy as np
import random

def generate_trials(n_trials=200 , ratio_oddball=0.2) -> np.ndarray:
    trials = np.zeros(n_trials, dtype=int)
    
    # randomize oddball positions
    idx_odd = np.sort(np.array(random.sample(
        range(0, n_trials),
        int(n_trials * ratio_oddball)
    )))
    # ensure no consecutive oddballs and starts with standard
    while any(np.diff(idx_odd) <= 1) or idx_odd[0] < 4:
        idx_odd = np.sort(np.array(random.sample(
            range(0, n_trials),
            int(n_trials * ratio_oddball)
        )))

    trials[idx_odd] = 1
    
    return trials

def generate_isis(n_trials=200, min=2.0, max=3.0) -> np.ndarray:
    return np.random.uniform(min, max, n_trials)

# test
if __name__ == "__main__":
    trials = generate_trials(100, 0.2)
    print(trials)
    isis = generate_isis(100, 2.0, 3.0)
    print(isis)
    print(isis.sum())