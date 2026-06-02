from psychopy import visual, core

win = visual.Window([400, 400])
gabor = visual.GratingStim(win, tex='sin', mask='gauss', sf=5, name='gabor')
gabor.autoDraw = True
gabor.autoLog = False

clock = core.Clock()
while clock.getTime() < 2.0:
    if 0.5 <= clock.getTime() < 1.0:
        gabor.phase += 0.1
    win.flip()