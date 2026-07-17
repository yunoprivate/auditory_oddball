# main.py
from psychopy import prefs
import psychtoolbox.audio as audio

# Set PTB
prefs.hardware['audioLib'] = ['ptb'] # type: ignore

# Set Speaker
headphone = 'スピーカー'
for dev in audio.get_devices():
    if (dev['NrOutputChannels'] > 0 
        and dev['HostAudioAPIName'] == 'Windows WASAPI' 
        and headphone in dev['DeviceName']):
        prefs.hardware['audioDevice'] = dev['DeviceName'] # type: ignore

from psychopy import visual, core, event
from pyglet.canvas import get_display
from arduino import DummyTTL, connect_arduino
from AuditoryOddball import AuditoryOddball
from csv_writer import csv_writer

import csv
from pathlib import Path

def ask_int(prompt: str, default: int) -> int:
    text = input(f'{prompt} [{default}]: ').strip()
    return default if text == '' else int(text)

def ask_float(prompt: str, default: float) -> float:
    text = input(f'{prompt} [{default}]: ').strip()
    return default if text == '' else float(text)

def main():
    print('=== Auditory Oddball Settings ===')

    n_trials = ask_int('Number of trials', 200)
    ratio_oddball = ask_float('Oddball ratio', 0.2)
    freq_standard = ask_float('Standard frequency (Hz)', 1000.0)
    freq_target = ask_float('Target frequency (Hz)', 2000.0)
    
    arduino = connect_arduino()

    test = AuditoryOddball(
        n_trials=10,
        ratio_oddball=0.2,
        freq_standard=freq_standard,
        freq_target=freq_target,
        arduino=DummyTTL()
    )
    trial1 = AuditoryOddball(
        n_trials=n_trials,
        ratio_oddball=ratio_oddball,
        freq_standard=freq_standard,
        freq_target=freq_target,
        arduino=arduino,
    )
    trial2 = AuditoryOddball(
        n_trials=n_trials,
        ratio_oddball=ratio_oddball,
        freq_standard=freq_standard,
        freq_target=freq_target,
        arduino=arduino,
    )

    screens = get_display().get_screens()
    screen_id = 1 if len(screens) > 1 else 0

    win = visual.Window(
        #fullscr=True,
        screen=screen_id,
        color='black',
        units='height',
    )
    """
    qr = visual.ImageStim(
        win,
        image='qrcode/tdms.png',
    )
    """
    instraction = visual.TextStim(
        win,
        text='press SPACE to start',
        height=0.04,
    )
    fixation = visual.TextStim(
        win,
        text='+',
        height=0.08,
    )

    logs = []

    #qr.draw()
    instraction.draw()
    win.flip()
    event.waitKeys(keyList=['space'])

    fixation.draw()
    win.flip()

    test.generate()
    logs.append(test.run())
    
    instraction.draw()
    win.flip()
    event.waitKeys(keyList=['space'])

    fixation.draw()
    win.flip()

    trial1.generate()
    logs.append(trial1.run())

    instraction.draw()
    win.flip()
    event.waitKeys(keyList=['space'])

    fixation.draw()
    win.flip()

    trial2.generate()
    logs.append(trial2.run())    

    csv_writer('data', logs, 'TEST')

    arduino.close()

if __name__ == '__main__':
    main()