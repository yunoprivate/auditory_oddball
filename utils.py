# utils.py
import numpy as np
import random

def generate_stims(
        n_stims=200,
        ratio_oddball=0.2,
        jitter=1,
    ) -> np.ndarray:
    '''Generate stimuli array
    
    n_stims: number of stimuli
    ratio_oddball: ratio of oddball
    jitter: variation in intervals

    TTI is determined by the ratio of oddball and the valiation in intervals.

    TTI = (1 / ratio_oddball) ± jitter
    '''
    if not 0 < ratio_oddball < 1:
        raise ValueError('ratio_oddball must be between 0 and 1')
    
    n_targets = round(n_stims * ratio_oddball)
    tti_mean = round(1 / ratio_oddball)

    stims = np.zeros(n_stims, dtype=int)

    # ensure 

def generate_trials(n_trials=200 , ratio_oddball=0.2) -> np.ndarray:
    '''Generate stimuli array with random ISI
    '''
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
    trials = generate_trials(200, 0.2)
    print(trials)
    isis = generate_isis(200, 2.0, 3.0)
    print(isis)
    print(isis.sum())

    total = 0
    for i in range(10):
        total += generate_isis().sum()

    print(total/10)