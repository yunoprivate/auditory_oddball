from pathlib import Path
from scipy.io import wavfile
import numpy as np

def create_sound(path, freq):
    fs = 48000
    duration = 50/1000
    fade = 5/1000
    
    t = np.arange(0, duration, 1/fs)
    sound = np.sin(2*np.pi*freq*t)

    fade_samples = int(fs * fade)
    fade_in = np.linspace(0, 1, fade_samples)
    fade_out = fade_in[::-1]

    envelope = np.ones_like(sound)
    envelope[:fade_samples] = fade_in
    envelope[-fade_samples:] = fade_out

    sound *= envelope

    wavfile.write(path, fs, sound.astype(np.float32))

def fetch_sound(freq) -> Path:
    sound_dir = Path('sound')
    sound_dir.mkdir(exist_ok=True)

    sound_file = sound_dir / f'{freq}Hz.wav'
    if not sound_file.is_file():
        create_sound(sound_file, freq)
    
    return sound_file

if __name__ == "__main__":
    from psychopy import prefs
    prefs.hardware['audioLib'] = ['ptb']
    from psychopy import sound, core

    freq_standard = 500
    freq_target = 1000

    standard = sound.Sound(fetch_sound(freq_standard))
    target = sound.Sound(fetch_sound(freq_target))
    
    standard.play()
    core.wait(2)
    target.play()
    core.wait(2)