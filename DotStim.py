import pandas as pd
from psychopy.gui import DlgFromDict
from psychopy.visual import Window, TextStim, ImageStim, Rect, TextBox, DotStim
from psychopy.core import Clock, quit, wait
from psychopy.event import Mouse
from psychopy.hardware.keyboard import Keyboard
from psychopy import event, data
import random
### DIALOG BOX ROUTINE ###
exp_info = {'participant_nr': '', 'age': '','number of trials':[10,50,100,150]} #the "" means an empty box. 
dlg = DlgFromDict(exp_info)
trialn= exp_info['number of trials']

# Initialize a fullscreen window with my monitor (HD format) size
# and my monitor specification called "samsung" from the monitor center
win = Window(size=(1200, 800), fullscr=False, monitor='samsung')

# Also initialize a mouse, although we're not going to use it
mouse = Mouse(visible=False)

# Initialize a (global) clock
clock = Clock()

# Initialize Keyboard
kb = Keyboard()
kb.clearEvents()

### WELCOME ROUTINE ###
# Create a welcome screen and show for 2 seconds
welcome_txt_stim = TextStim(win, text="Welcome to this experiment!", color=(1, 0, -1), font='Calibri')
welcome_txt_stim.draw()
win.flip()
wait(2)

## collect participant number again
instruct_txt = """ 
Please type the first four letters of your last name followed by the last two digits of your birth year. 
When you are finished, hit the return key.
"""
instruct=TextStim(win,instruct_txt,pos=(0,0.75))
instruct.draw()
win.flip()
# Initialize keyboard and wait for response
kb = Keyboard()
p_name='' #blank
while True:
    keys = kb.getKeys()
    for key in keys:
        p_name=p_name+key.name #that means the typed somethig, well actually prints to us which keys they pressed 
        display=TextStim(win,p_name)
        display.draw() #display it to them 
        instruct.draw()
        win.flip()
    if 'return' in keys:
        p_name=p_name
        break  # break out of the loop!

### INSTRUCTION ROUTINE ###
task_instruct_txt = """ 
In this experiment, you will see a collection of moving dots.

On each trial the predominant movement of the dots will either be towards the top or the bottom.

You should indicate with the arrow keys which direction the motion is in. 

Sometimes it may be hard to tell; go with your best guess!
    
 """

# Show instructions and wait until response (return)
task_instruct_txt = TextStim(win, task_instruct_txt, alignText='left', height=0.085)
task_instruct_txt.draw()
win.flip()

# Initialize keyboard and wait for response
kb = Keyboard()
while True:
    keys = kb.getKeys()
    if 'return' in keys:
        break  # break out of the loop!

# Configuration parameters
N_TRIALS = trialn #fixing or changing in the experiment, a varibale you are changing 
N_DOTS = 150
DOT_SIZE = 5  # in pixels
DOT_SPEED = 0.5  # degrees/frame
DOT_FIELD_SIZE = 2  # degrees, how big the colelction of dots is 
COHERENCE_LEVELS = [0.05, 0.1, 0.2, 0.4, 0.8]  # Fixed coherence levels, by changing this how obious is the motion the dots are moving in 
DIRECTIONS = [90, 270]  # UP (90°) and DOWN (270°)
FIXATION_MIN = 0.5  # seconds
FIXATION_MAX = 1.5  

# Create fixation and dots stimuli once (more efficient)
fix = TextStim(win, "+", height=2)
dots = DotStim( 
    win, #projected to the window 
    fieldShape='circle', 
    nDots=N_DOTS, #150
    fieldSize=DOT_FIELD_SIZE, 
    dotSize=DOT_SIZE,
    speed=DOT_SPEED,
    dotLife=-1,  # infinite lifetime
    noiseDots='direction', #adding radnom noise to the dots 
    signalDots='same' #one core direction 
)

trialn=int(trialn)
# Create trial handler for proper randomization and data collection
trial_list = []
for coherence in COHERENCE_LEVELS: #we defined what the coherence levels is 
    for direction in DIRECTIONS: #up or down, bc we defined that 
        # Multiple repetitions of each condition
        for rep in range(0,trialn//10):  #create a spredsheet to show I got 10 different conditions, range is 0,5 run through the loop 5 times  
            trial_list.append({   #50 trials then divided by 10 is 5 so 
                'coherence': coherence,
                'direction': direction, #90 or 270 
                'correct_response': 'up' if direction == 90 else 'down'
            })

trials = data.TrialHandler(trial_list, nReps=1, method='random') #mix all these trials up 
# Main experiment loop
for trial in trials:
    # Variable fixation period (prevents anticipation)
    fixation_time = random.uniform(FIXATION_MIN, FIXATION_MAX) #a random time between 0.5 and 1.5 seconds 
    
    # Show fixation
    fix.draw()
    win.flip()
    wait(fixation_time)
    
    # Set dot parameters for this trial
    dots.coherence = trial['coherence'] #the extent on the dots moving together 
    dots.dir = trial['direction'] 
    
    # Reset keyboard and clock
    kb.clock.reset()
    kb.clearEvents()
    
    # Present dots and collect response
    response = None
    rt = None
    
    while response is None:
        dots.draw()
        win.flip()
        
        # Check for response
        keys = kb.getKeys(['up', 'down', 'escape'], waitRelease=False)
        if keys:
            response = keys[0].name
            rt = keys[0].rt
            
            # Allow escape to quit
            if response == 'escape':
                win.close()
                quit()
    
    # Record trial data
    trials.addData('response', response) #adding data to the sheet calling it response and reporting their response 
    trials.addData('rt', rt)
    trials.addData('correct', response == trial['correct_response']) #did they make the correct repsonse? 
    trials.addData('fixation_duration', fixation_time)
    
    # Brief inter-trial interval
    win.flip()
    wait(0.5)

# Save data
filename = p_name + '_random_dot_motion'
trials.saveAsExcel(filename + '.xlsx')

# Show completion message
end_text = visual.TextStim(win, "Task complete! Thank you.", height=1)
end_text.draw()
win.flip()
wait(2)

win.close()
quit()







