from psychopy import prefs
# Set PTB
prefs.hardware['audioLib'] = ['ptb'] # type: ignore

import psychtoolbox.audio
# If exist, set Speaker
headphone = 'スピーカー (High Definition Audio Device)'
for dev in psychtoolbox.audio.get_devices():
    if (dev['NrOutputChannels'] > 0 
        and dev['HostAudioAPIName'] == 'Windows WASAPI' 
        and headphone in dev['DeviceName']):
        prefs.hardware['audioDevice'] = headphone # type: ignore

from psychopy import visual, core, event
from arduino import DummyTTL, connect_arduino
from AuditoryOddball import AuditoryOddball

def ask_int(prompt: str, default: int) -> int:
    try:
        value = int(input(f'{prompt} [{default}]: ').strip())
    except ValueError:
        value = default
    return value

def ask_float(prompt: str, default: float) -> float:
    try:
        value = float(input(f'{prompt} [{default}]: ').strip())
    except ValueError:
        value = default
    return value

def main():
    print('=== Auditory Oddball Settings ===')

    n_trials = ask_int('Number of trials', 200)
    ratio_oddball = ask_float('Oddball ratio', 0.2)
    freq_standard = ask_float('Standard frequency (Hz)', 1000.0)
    freq_target = ask_float('Target frequency (Hz)', 2000.0)

    arduino = connect_arduino()

    win = visual.Window(
        fullscr=True,
        screen=1, # 0 for Main monitor, 1 for Sub monitor
        color='black',
        units='height',
    )
    generating = visual.TextStim(
        win,
        text='Generating Trials...',
        height=0.04
    )
    instraction = visual.TextStim(
        win,
        text='Press SPACE to start',
        height=0.04,
    )
    fixation = visual.TextStim(
        win,
        text='+',
        height=0.08,
    )

    logs = []

    
