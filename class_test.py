from psychopy import sound, core
import numpy as np
import generate_trials

class AuditoryOddball:
    def __init__(self, paths, config):
        self.paths = paths
        self.config = config
        self.__prep()

    def __prep(self):
        standard = sound.Sound(self.paths["standard"])
        target = sound.Sound(self.paths["target"])
        
        self.trials = generate_trials(
            self.config["n_trials"],
            self.config["ratio_oddball"]
        )

        self.isis = np.random.uniform(2.0, 3.0, self.config["n_trials"])

        self.trial_info = {
            0: {
                "stimli": standard,
                "ttl": b"1"
            },
            1: {
                "stimli": target,
                "ttl": b"2"
            }
        }

    def run(self):
        pass