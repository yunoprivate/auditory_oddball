from psychopy import prefs

# set audioLib to ptb
prefs.hardware['audioLib'] = ['ptb']

from psychopy import sound
print(sound.Sound)