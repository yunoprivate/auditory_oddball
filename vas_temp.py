from psychopy import visual, event, core

def run_vas(min_val=0, max_val=100, start_val=None, step=1):
    """
    Display a Visual Analog Scale (VAS) in PsychoPy and return the selected value.
    :param min_val: Minimum value on the scale
    :param max_val: Maximum value on the scale
    :param start_val: Starting position of the marker (default: middle)
    :param step: Step size for marker movement
    :return: Selected value
    """
    # Create PsychoPy window
    win = visual.Window(size=(800, 600), color="black", units="pix")

    # Create the scale
    vas = visual.Slider(
        win, 
        ticks=(1, 2, 3, 4, 5)        
    )

    # Instruction text
    instruction = visual.TextStim(win, text="Use LEFT/RIGHT arrows to move.\nPress ENTER to confirm.",
                                  color="white", pos=(0, 150), height=24)

    # Main loop
    while True:
        instruction.draw()
        vas.draw()
        win.flip()

        # Allow quitting with ESC
        if 'escape' in event.getKeys():
            win.close()
            core.quit()
            break

    # Get the selected value
    selected_value = vas.getRating()

    # Show confirmation
    confirm_text = visual.TextStim(win, text=f"You selected: {selected_value}",
                                   color="white", pos=(0, 0), height=30)
    confirm_text.draw()
    win.flip()
    core.wait(10)

    win.close()
    return selected_value


if __name__ == "__main__":
    try:
        value = run_vas(min_val=0, max_val=10, step=0.1)
        print(f"Final selected value: {value}")
    except Exception as e:
        print(f"Error: {e}")
