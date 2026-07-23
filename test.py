from psychopy import visual

win = visual.Window(
    fullscr=False,
    screen=1,
    color='black',
    units='height',
)

instrustion = visual.TextStim(
    win=win,
    text='',
    pos=(0, 0),
    height=0.045,
    color='white',
    wrapWidth=1.45,
    alignText='center',
    anchorHoriz='center',
    anchorVert='center',
)

fixation = visual.TextStim(
    win=win,
    text='+',
    pos=(0, 0),
    height=0.08,
    color='white',
)

countdown = visual.TextStim(
    win=win,
    text='',
    pos=(0, 0),
    height=0.12,
    color='white',
)

# ----------------------------------------------------------------------
# 表示文章
# ----------------------------------------------------------------------

PRACTICE_INSTRUCTION = '''
これから練習を行います．

低い音と高い音がランダムに流れます．
高い音が鳴ったときに，SPACEキーを押してください．

準備ができたらSPACEキーを押してください．
'''.strip()


PRACTICE_FINISHED = '''
練習は終了です．

音量や操作方法に問題がある場合は，
実験者に伝えてください．

問題がなければ，SPACEキーを押してください．
'''.strip()


REST_INSTRUCTION = '''
これから2分間，静かにお待ちください．

できるだけ身体を動かさず，
リラックスして過ごしてください．

終了時に音が鳴ります．

準備ができたらSPACEキーを押してください．
'''.strip()


REST_FINISHED = '''
終了です．

続いてアンケートに回答してください．
'''.strip()


QUESTIONNAIRE_INSTRUCTION = '''
アンケートに回答してください．

回答が完了したらSPACEキーを押してください．
'''.strip()


ODDBALL_1_INSTRUCTION = '''
これから1回目の課題を行います．

高い音が鳴ったときに，
SPACEキーを押してください．

準備ができたらSPACEキーを押してください．
'''.strip()


ODDBALL_1_FINISHED = '''
1回目の課題は終了です．

続いてアンケートに回答してください．
'''.strip()


ANGER_RECALL_INSTRUCTION = '''
これから2分間，
過去に強い怒りを感じた出来事を思い出してください．

そのときの場所，相手の表情や言葉，
自分が感じたことなどを，
できるだけ具体的に思い出してください．

想起中は，その出来事について考え続けてください．
終了時に音が鳴ります．

準備ができたらSPACEキーを押してください．
'''.strip()


ANGER_RECALL_FINISHED = '''
怒り想起は終了です．

続いてアンケートに回答してください．
'''.strip()


ODDBALL_2_INSTRUCTION = '''
これから2回目の課題を行います．

高い音が鳴ったときに，
SPACEキーを押してください．

準備ができたらSPACEキーを押してください．
'''.strip()


ODDBALL_2_FINISHED = '''
2回目の課題は終了です．

最後にアンケートに回答してください．
'''.strip()


EXPERIMENT_FINISHED = '''
以上で実験は終了です．

ご協力ありがとうございました．
'''.strip()

from psychopy import event

def show_message(
        stim: visual.TextStim,
        message: str,
        key_list: list[str] | None = None,
) -> list[str] | None:
    '''
    文章を画面に表示する．
    
    key_list が指定された場合は，キー入力まで待機する．
    指定されていない場合は，表示だけ行う．
    '''
    stim.text = message
    stim.draw()
    win.flip()

    if key_list is not None:
        return event.waitKeys(keyList=key_list)
    
    return None

from psychopy import core

def show_countdown(seconds: int = 3) -> None:
    for number in range(seconds, 0, -1):
        countdown.text = str(number)
        countdown.draw()
        win.flip()
        core.wait(1.0)
    
    countdown.text = '開始'
    countdown.draw()
    win.flip()
    core.wait(0.5)

if __name__ == '__main__':
    print('message')
    show_message(
        instrustion,
        PRACTICE_INSTRUCTION,
        key_list=['space'],
    )
    print('countdown')
    show_countdown()