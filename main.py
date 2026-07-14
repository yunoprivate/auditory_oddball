# main.py
from psychopy import prefs
# Select PTB
prefs.hardware['audioLib'] = ['ptb'] # type: ignore
from psychopy import visual, core, event
from pyglet.canvas import get_display
from arduino import connect_arduino
from AuditoryOddball import AuditoryOddball

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
    ttl = connect_arduino()

    trial = AuditoryOddball(
        n_trials=n_trials,
        ratio_oddball=ratio_oddball,
        freq_standard=freq_standard,
        freq_target=freq_target,
        ttl=ttl,
    )

    screens = get_display().get_screens()
    screen_id = 1 if len(screens) > 1 else 0

    win = visual.Window(
        #fullscr=True,
        screen=screen_id,
        color='black',
        units='height',
    )
    qr = visual.ImageStim(
        win,
        image='qrcode/tdms.png',
    )
    instraction = visual.TextStim(
        win,
        text='press SPACE to start',
        pos=(0,-0.3),
        height=0.04,
    )
    fixation = visual.TextStim(
        win,
        text='+',
        height=0.08,
    )

    qr.draw()
    instraction.draw()
    win.flip()
    event.waitKeys(keyList=['space'])

    fixation.draw()
    win.flip()

    logs = trial.run()
    #print(logs)

    Path("data").mkdir(exist_ok=True)

    if(logs):
        with open('data/oddball_log.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=logs[0].keys())
            writer.writeheader()
            writer.writerows(logs)
    
    ttl.close()

if __name__ == '__main__':
    main()