# AuditoryOddball.py
import psychtoolbox as ptb
import numpy as np
from utils import generate_trials, generate_isis
from arduino import DummyTTL, TTLSender
from audio import fetch_sound

class AuditoryOddball:
    def __init__(
            self,
            ttl: TTLSender | DummyTTL,
            n_trials=200,
            ratio_oddball=0.2,
            freq_standard=1000.0, 
            freq_target=2000.0,
        ):
        self.ttl = ttl
        self.standard = freq_standard
        self.target = freq_target
        self.n_trials = n_trials
        self.ratio = ratio_oddball
        self.__prep()

    def __prep(self):
        standard = fetch_sound(self.standard)
        target = fetch_sound(self.target)
        
        self.trials = generate_trials(
            self.n_trials,
            self.ratio
        )

        self.isis = generate_isis(self.n_trials)

        self.trial_info = {
            0: {
                'stim': standard,
                'ttl': 1
            },
            1: {
                'stim': target,
                'ttl': 2
            }
        }

    def run(self):
        '''
        run auditory oddball task
        '''
        onset = ptb.GetSecs() + 1.0

        for trial, isi in zip(self.trials, self.isis):
            info = self.trial_info[trial]

            while ptb.GetSecs() < onset:
                pass

            self.ttl.send(info['ttl'])
            info['stim'].play()

            onset += isi