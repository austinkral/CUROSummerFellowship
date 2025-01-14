from psychopy import visual, core, data, event, logging, gui, prefs
from psychopy.hardware import keyboard
from psychopy import monitors
from psychopy.visual import TextStim
import csv
import os, random, numpy as np
from itertools import permutations

# Prompt user for participant number
expName='MICWCI'
expInfo={'Participant Number':''}
dlg=gui.DlgFromDict(dictionary=expInfo,title=expName)
if dlg.OK==False: core.quit() #user pressed cancel
expInfo['date']=data.getDateStr() #add a simple timestamp
expInfo['expName']=expName
sbjIdx = str(expInfo['Participant Number'])

# Parent directory path for lab computer
parent_dir = r"C:\Users\Public\Desktop\Public Documents\Austin\MICWCI\data"
fileName = parent_dir + os.path.sep +'%s_%s_%s' %(expName, sbjIdx, expInfo['date'])

# Make a csv file to save data
dataFile = open(fileName+'.csv', 'w')
dataFile.write('trialNum,' 'imgNum,' 'rating\n') # you need a comma to separate columns
data=[]

# Create keyboard
kb = keyboard.Keyboard()
userInput = ['1','2','3','4','5','6','7']

# Create a window to draw in
win = visual.Window(monitor='MIC+WCI', allowGUI=False, color=(255, 255, 255), 
colorSpace="rgb255", units='pix', fullscr=True)
    
# Intro slide
intro = visual.TextStim(win, 'INTRODUCTION', pos=(0, 50), color=(0,0,0), 
colorSpace='rgb255',wrapWidth=750, height=30)
# Part I Demo slide
partIDemo= visual.TextStim(win, 'PART I: Rating Demonstration', pos=(0, 50), 
color=(0,0,0), colorSpace='rgb255', wrapWidth=750, height=30)
# Part I slide
partI = visual.TextStim(win, 'PART I', pos=(0, 50), color=(0,0,0), 
colorSpace='rgb255', wrapWidth=750, height=30)
# Part II Demo slide
partIIDemo = visual.TextStim(win, 'PART II: Shading Demonstration', pos=(0, 50), 
color=(0,0,0), colorSpace='rgb255', wrapWidth=750, height=30)
# Part II slide
partII = visual.TextStim(win, 'PART II', pos=(0, 50), color=(0,0,0), 
colorSpace='rgb255', wrapWidth=750, height=30)
# Advance slides
begin = visual.TextStim(win, 'Press <SPACE> when you are ready to begin.', 
pos=(0, -225  ), color=(0,0,0), colorSpace='rgb255', wrapWidth=750, height=24)
advance = visual.TextStim(win, 'Press <SPACE> to continue.', pos=(0, -225 ), 
color=(0,0,0), colorSpace='rgb255', wrapWidth=750, height=30)
# Rating slides
rating = visual.TextStim(win, 'Please rate the stimulus above on the ' +
'following scale:', pos=(0, -110), color=(0,0,0), colorSpace='rgb255', 
wrapWidth=750, height=30)
scaleTxt = visual.TextStim(win, '1 - 7', pos=(0, -205), color=(0,0,0), 
colorSpace='rgb255', wrapWidth=750, height=30)
# Outro slide
outro = visual.TextStim(win, 'The experiment is now concluded.\nThank you '
'for your participation.', color=(0, 0, 0), colorSpace='rgb255', height=30)

# Intro images
WCI = visual.ImageStim(win, image='images/example(square).png', units='pix', 
pos=[0,0])
scale = visual.ImageStim(win, image='images/scale.png', units='pix', 
pos=[0,-65])
ratingExample = visual.ImageStim(win, image='images/ratingExample.png', 
units='pix', pos=[0,0])
shadingExample = visual.ImageStim(win, image='images/shadingExample.png',
units='pix', pos=[0,0])

# Create ratings static list
img1= visual.ImageStim(win, filename='static/plain4.gif', 
units='pix', size=[800,600], pos=[0, 0], autoLog=False)
img2= visual.ImageStim(win, filename='static/plain6.gif', 
units='pix', size=[800,600], pos=[0, 0], autoLog=False)
img3= visual.ImageStim(win, filename='static/stripes4.gif', 
units='pix', size=[800,600], pos=[0, 0], autoLog=False)
img4= visual.ImageStim(win, filename='static/stripes6.gif', 
units='pix', size=[800,600], pos=[0, 0], autoLog=False)
img5= visual.ImageStim(win, filename='static/floatingFringe4.gif',  
units='pix', size=[800,600], pos=[0, 0], autoLog=False)
img6= visual.ImageStim(win, filename='static/overhang4.gif', 
units='pix', size=[800,600], pos=[0, 0], autoLog=False)
img7= visual.ImageStim(win, filename='static/overhangGap4.gif', 
units='pix', size=[800,600], pos=[0, 0], autoLog=False)
imgListRatings = [img1, img2, img3, img4, img5, img6, img7]

# Create shadings static list
img1= visual.ImageStim(win, filename='static/plain4v2.gif', 
units='pix', size=[800,600], pos=[0, 0], autoLog=False)
img2= visual.ImageStim(win, filename='static/plain6v2.gif', 
units='pix', size=[800,600], pos=[0, 0], autoLog=False)
img3= visual.ImageStim(win, filename='static/stripes4v2.gif', 
units='pix', size=[800,600], pos=[0, 0], autoLog=False)
img4= visual.ImageStim(win, filename='static/stripes6v2.gif', 
units='pix', size=[800,600], pos=[0, 0], autoLog=False)
img5= visual.ImageStim(win, filename='static/floatingFringe4v2.gif',  
units='pix', size=[800,600], pos=[0, 0], autoLog=False)
img6= visual.ImageStim(win, filename='static/overhang4v2.gif', 
units='pix', size=[800,600], pos=[0, 0], autoLog=False)
img7= visual.ImageStim(win, filename='static/overhangGap4v2.gif', 
units='pix', size=[800,600], pos=[0, 0], autoLog=False)
imgListShadings = [img11, img12, img13, img14, img15, img16, img17]

# Randomize presentation order for each trial
perm1 = np.random.permutation([0, 1, 2, 3, 4, 5, 6])
perm2 = np.random.permutation([0, 1, 2, 3, 4, 5, 6])
perm3 = np.random.permutation([0, 1, 2, 3, 4, 5, 6])
perm4 = np.random.permutation([0, 1, 2, 3, 4, 5, 6])

# Introduction
intro.draw()
win.flip()
event.waitKeys(keyList=['space'])
# Watercolor illusion example
WCI.draw()
win.flip()
event.waitKeys(keyList=['space'])
# Rating Demo
partIDemo.draw()
advance.draw()
win.flip()
event.waitKeys(keyList=['space'])
ratingExample.draw()
rating.draw()
scaleTxt.draw()
win.flip()
event.waitKeys(keyList=['1','2','3','4','5','6','7'])
# Part I
partI.draw()
begin.draw()
win.flip()
event.waitKeys(keyList=['space'])
kb.clearEvents()
trial = 0
for i in range(7):
    imgListRatings[perm1[i]].draw()
    rating.draw()
    scaleTxt.draw()
    win.flip()
    keys = kb.getKeys(['1','2','3','4','5','6','7'], waitRelease=True)
    if any(elem in keys for elem in userInput):
        response = int(keys[0].name)
    trial = trial+1
    data.append(['1'])
    data[trial - 1].append(perm1[i])
    data[trial - 1].append(response)
    # Join the elements in a row with a string separator, comma (csv)
    line = ','.join(str(a) for a  in data[trial - 1]) 
    line += '\n' # indicates the end of a line
    # Write the line 
    dataFile.write(line)
    # flush() cleans out the internal buffer when writing to a file.
    dataFile.flush()
    os.fsync(dataFile) # forces write of the file
# Trial 2
for i in range(7):
    imgListRatings[perm2[i]].draw()
    rating.draw()
    scaleTxt.draw()
    win.flip()
    keys = kb.getKeys(['1','2','3','4','5','6','7'], waitRelease=True)
    if any(elem in keys for elem in userInput):
        response = int(keys[0].name)
    trial = trial + 1
    data.append(['2'])
    data[trial - 1].append(perm2[i])
    data[trial - 1].append(response)
    # Join the elements in a row with a string separator, comma (csv)
    line = ','.join(str(a) for a  in data[trial - 1])
    line += '\n'
     # Write the line 
    dataFile.write(line)
    # flush() cleans out the internal buffer when writing to a file
    dataFile.flush()
    os.fsync(dataFile) # forces write of the file
    written = True
# Trial 3
for i in range(7):
    imgListRatings[perm3[i]].draw()
    rating.draw()
    scaleTxt.draw()
    win.flip()
    keys = kb.getKeys(['1','2','3','4','5','6','7'], waitRelease=True)
    if any(elem in keys for elem in userInput):
        response = int(keys[0].name)
    trial = trial + 1
    data.append(['3'])
    data[trial - 1].append(perm3[i])
    data[trial - 1].append(response)
    # Join the elements in a row with a string separator, comma (csv)
    line = ','.join(str(a) for a  in data[trial - 1])
    line += '\n'
     # Write the line 
    dataFile.write(line)
    # flush() cleans out the internal buffer when writing to a file.
    dataFile.flush()
    os.fsync(dataFile) # forces write of the file
    written = True
# Shading Demo
partIIDemo.draw()
advance.draw()
win.flip()
event.waitKeys(keyList=['space'])
shadingExample.draw()
win.flip()
event.waitKeys(keyList=['space'])
# Trial 4: Shading
partII.draw()
begin.draw()
win.flip()
event.waitKeys(keyList=['space'])
kb.clearEvents()
for i in range(7):
    imgListShadings[perm4[i]].draw()
    win.flip()
    event.waitKeys(keyList=['space']
# End screen
outro.draw()
win.flip()
core.wait(3.0)
win.close()
core.quit()