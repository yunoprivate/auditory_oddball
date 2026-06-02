from psychopy import visual, core

win = visual.Window([400, 400])
gabor = visual.GratingStim(win, tex='sin', mask='gauss', sf=5, name='gabor', autoLog=False)
fixation = visual.GratingStim(win, tex=None, mask='gauss', sf=0, size=0.02, name='fixation', autoLog=False)

for frameN in range(200):
    if 10 <= frameN < 150:
        fixation.draw()
    if 50 <= frameN < 100:
        gabor.phase += 0.1
        gabor.draw()
    win.flip()