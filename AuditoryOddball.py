# AuditoryOddball.py
import psychtoolbox as ptb
import numpy as np
from utils import generate_trials, generate_isis
#from arduino import TTLSender
from audio import fetch_sound

class AuditoryOddball:
    def __init__(self, freqs: dict, config: dict):
        self.freqs = freqs
        self.config = config
        self.__prep()

    def __prep(self):
        standard = fetch_sound(self.freqs['standard'])
        target = fetch_sound(self.freqs['target'])
        
        self.trials = generate_trials(
            self.config['n_trials'],
            self.config['ratio_oddball']
        )

        self.isis = generate_isis(self.config['n_trials'])

        self.trial_info = {
            0: {
                'stim': standard,
                'ttl': b'1'
            },
            1: {
                'stim': target,
                'ttl': b'2'
            }
        }

        #self.ttl = self.config['ttl']

    def run(self):
        '''
        run auditory oddball paradigm
        '''
        onset = ptb.GetSecs() + 1.0

        for trial, isi in zip(self.trials, self.isis):
            info = self.trial_info[trial]

            while ptb.GetSecs() < onset:
                pass

            #self.ttl.send(info['ttl'])
            info['stim'].play()

            onset += isi