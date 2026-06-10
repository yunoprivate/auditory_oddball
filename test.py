from psychopy import prefs
# Select PTB
prefs.hardware['audioLib'] = ['ptb']
from psychopy import visual, core, event
from AuditoryOddball import AuditoryOddball

win = visual.Window(
    size=(1280, 720),
    color='black',
    units='height',
)

fixation = visual.TextStim(
    win,
    text='+',
    color='white',
    height=0.08,
)

instruction = visual.TextStim(
    win,
    text='press SPACE to start',
    color='white',
    height=0.04,
)

instruction.draw()
win.flip()
event.waitKeys(keyList=['space'])

fixation.draw()
win.flip()

freqs = {
    'standard': 500.0,
    'target': 1000.0
}
config = {
    'n_trials': 100,
    'ratio_oddball': 0.2
}

trial = AuditoryOddball(freqs, config)
trial.run()

core.wait(2)