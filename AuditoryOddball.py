# AuditoryOddball.py
from psychopy.hardware import keyboard
from psychopy import core
import psychtoolbox as ptb
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
                'ttl': b'1'
            },
            1: {
                'stim': target,
                'ttl': b'2'
            }
        }

    def run(self):
        '''
        run auditory oddball task
        return log
        '''
        kb = keyboard.Keyboard()

        ptb_clock = ptb.GetSecs() + 1.0

        logs = []
        log_clock = core.Clock()
        log_clock.reset()

        for i, (trial, isi) in enumerate(zip(self.trials, self.isis)):
            info = self.trial_info[trial]

            kb.clearEvents()
            response_time = None
            responded = False
            
            ttl_time = log_clock.getTime()
            print(info['ttl'])
            self.ttl.send(info['ttl'])

            play_time = log_clock.getTime()
            info['stim'].play()

            next_onset = ptb_clock + isi

            while ptb.GetSecs() < next_onset:
                keys = kb.getKeys(['space', 'escape'], waitRelease=False)

                for key in keys:
                    if key.name == 'escape':
                        return logs
                    if key.name == 'space' and not responded:
                        response_time = log_clock.getTime()
                        responded = True
                        break

                core.wait(0.001)

            logs.append({
                'trial_index': i,
                'trial_type': int(trial),
                'ttl_sent_time': ttl_time,
                'stim_played_time': play_time,
                'response_time': response_time,
                'responded': responded,
            })

            ptb_clock = next_onset

        return logs