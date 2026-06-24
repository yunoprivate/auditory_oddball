# main.py
from psychopy import prefs
# Select PTB
prefs.hardware['audioLib'] = ['ptb']
from psychopy import visual, core, event
from arduino import TTLSender, find_arduino
from AuditoryOddball import AuditoryOddball

win = visual.Window(
    size=(1280, 720),
    color='black',
    units='height',
)
fixation = visual.TextStim(
    win,
    text='+',
    height=0.08,
)
qr = visual.ImageStim(
    win,
    image='qrcode/tdms.png'
)
instruction = visual.TextStim(
    win,
    text='press SPACE to start',
    height=0.04,
)

port = find_arduino()
ttl = None
if(port):
    ttl = TTLSender(port)

freqs = {
    'standard': 1000.0,
    'target': 2000.0
}
config = {
    'n_trials': 200,
    'ratio_oddball': 0.2,
    'ttl': ttl
}

trial = AuditoryOddball(freqs, config)
qr.draw()
win.flip()
core.wait(2)
instruction.draw()
win.flip()
event.waitKeys(keyList=['space'])

fixation.draw()
win.flip()

trial.run()

if(ttl):
    ttl.close()
