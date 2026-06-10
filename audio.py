# audio.py
from psychopy import sound
from pathlib import Path
from scipy.io import wavfile
import numpy as np

def create_sound(path: Path, freq: float, duration=50.0, fade=5.0, fs=48000):
    duration /= 1000
    fade /= 1000

    t = np.arange(0, duration, 1/fs)
    sound = np.sin(2*np.pi*freq*t)

    fade_samples = int(fs * fade)
    fade_in = np.linspace(0, 1, fade_samples)
    fade_out = fade_in[::-1]

    # Create fade
    envelope = np.ones_like(sound)
    envelope[:fade_samples] = fade_in
    envelope[-fade_samples:] = fade_out

    # Apply fade
    sound *= envelope
    
    wavfile.write(path, fs, sound.astype(np.float32))

def fetch_sound(freq, duration=50.0, fade=5.0) -> sound.Sound:
    sound_dir = Path('sound')
    sound_dir.mkdir(exist_ok=True)

    sound_file = sound_dir / f'{freq}Hz-{duration}ms-{fade}ms.wav'
    if not sound_file.is_file():
        create_sound(sound_file, freq, duration=duration, fade=fade)
    
    return sound.Sound(sound_file)
