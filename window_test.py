from psychopy import visual, core, event

win = visual.Window(
    size=(1280, 720),
    color="black",
    units="height"
)

fixation = visual.TextStim(
    win,
    text="+",
    color="white",
    height=0.08
)

instruction = visual.TextStim(
    win,
    text="中央の＋を見たまま音に注意してください。\n標的音が聞こえたらスペースキーを押してください。\n\nスペースキーで開始",
    color="white",
    height=0.04
)

instruction.draw()
win.flip()
event.waitKeys(keyList=["space"])

fixation.draw()
win.flip()

core.wait(2)

# ここでoddball開始