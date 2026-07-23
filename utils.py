# utils.py
import numpy as np
import random

def generate_stims(
        n=200,
        ratio=0.2,
    ) -> np.ndarray:
    '''Generate stimuli array
    
    n: number of stimuli
    ratio: ratio of oddball
    
    TTI is determined by the ratio of oddball.
    '''
    if not 0 < ratio < 1:
        raise ValueError('ratio must be between 0 and 1')

    stims = np.zeros(n, dtype=int)

    start = 3
    step = 1 / ratio
    target = n * ratio
    n1 = int(target * 0.5)
    n2 = int((target - n1) / 2)
    deviations = [0] * n1 + [-1, 1] * n2
    random.shuffle(deviations)
    while (np.any(np.abs(np.diff(deviations)) > 1)
           or deviations[0] == -1
           or deviations[-1] != deviations[0]):
        random.shuffle(deviations)

    for i, dev in enumerate(deviations):
        stims[start + int(i * step) + dev] = 1

    return stims

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
    stims = generate_stims()
    isis = generate_isis()
    print(stims)
    print(f'target: {sum(stims)}')
    print(f'total: {sum(isis)}')

    rare = [i for i, stim in enumerate(stims) if stim == 1]
    sum = 0
    for i in range(rare[0], rare[-1]):
        sum += isis[i]
    print(sum/39)