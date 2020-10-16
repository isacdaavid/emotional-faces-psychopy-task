#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.1),
    on octubre 14, 2019, at 18:37
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.0.1'
expName = 'emofaces'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='G:\\emofaces\\emofaces_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[800, 600], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Instrucciones:\n\nDurante los siguientes 6 minutos verás una serie de imágenes.\n\nMantén la atención en ellas e intenta no mover la cabeza.',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "instructions2"
instructions2Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Presiona un botón cada vez que notes un cambio en la imagen, utilizando los 2 botones de forma alternada:\n\nizq, der, izq, ...',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "instrucciones_3"
instrucciones_3Clock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Si piensas que la imagen es un hombre o una mujer, utiliza los botones así:\n\nizq:HOMBRE   der:MUJER\n\nPrepárate para iniciar..',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "start_2"
start_2Clock = core.Clock()
polygon_3 = visual.ShapeStim(
    win=win, name='polygon_3', vertices='cross',
    size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=.2, depth=0.0, interpolate=True)

# Initialize components for Routine "blank"
blankClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(.05, .05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=.2, depth=0.0, interpolate=True)

# Initialize components for Routine "scrambled"
scrambledClock = core.Clock()
image_5 = visual.ImageStim(
    win=win, name='image_5',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "happy"
happyClock = core.Clock()
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "sad"
sadClock = core.Clock()
image_2 = visual.ImageStim(
    win=win, name='image_2',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "angry"
angryClock = core.Clock()
image_3 = visual.ImageStim(
    win=win, name='image_3',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "neutral"
neutralClock = core.Clock()
image_4 = visual.ImageStim(
    win=win, name='image_4',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "happy"
happyClock = core.Clock()
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "sad"
sadClock = core.Clock()
image_2 = visual.ImageStim(
    win=win, name='image_2',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "angry"
angryClock = core.Clock()
image_3 = visual.ImageStim(
    win=win, name='image_3',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "neutral"
neutralClock = core.Clock()
image_4 = visual.ImageStim(
    win=win, name='image_4',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "scrambled"
scrambledClock = core.Clock()
image_5 = visual.ImageStim(
    win=win, name='image_5',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "blank"
blankClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(.05, .05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=.2, depth=0.0, interpolate=True)

# Initialize components for Routine "end"
endClock = core.Clock()
polygon_2 = visual.ShapeStim(
    win=win, name='polygon_2',
    vertices=[[-(0.5, 0.5)[0]/2.0,-(0.5, 0.5)[1]/2.0], [+(0.5, 0.5)[0]/2.0,-(0.5, 0.5)[1]/2.0], [0,(0.5, 0.5)[1]/2.0]],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=0, depth=0.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(15.000000)
# update component parameters for each repeat
# keep track of which components have finished
instructionsComponents = [text]
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructions"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    frameRemains = 0.0 + 15- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text.status == STARTED and t >= frameRemains:
        text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "instructions2"-------
t = 0
instructions2Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(15.000000)
# update component parameters for each repeat
# keep track of which components have finished
instructions2Components = [text_2]
for thisComponent in instructions2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructions2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = instructions2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    frameRemains = 0.0 + 15- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_2.status == STARTED and t >= frameRemains:
        text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions2"-------
for thisComponent in instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "instrucciones_3"-------
t = 0
instrucciones_3Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(15.000000)
# update component parameters for each repeat
# keep track of which components have finished
instrucciones_3Components = [text_3]
for thisComponent in instrucciones_3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instrucciones_3"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = instrucciones_3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    frameRemains = 0.0 + 15- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_3.status == STARTED and t >= frameRemains:
        text_3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrucciones_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instrucciones_3"-------
for thisComponent in instrucciones_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# ------Prepare to start Routine "start_2"-------
t = 0
start_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_11 = event.BuilderKeyResponse()
# keep track of which components have finished
start_2Components = [polygon_3, key_resp_11]
for thisComponent in start_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "start_2"-------
while continueRoutine:
    # get current time
    t = start_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_3* updates
    if t >= 0.0 and polygon_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_3.tStart = t
        polygon_3.frameNStart = frameN  # exact frame index
        polygon_3.setAutoDraw(True)
    
    # *key_resp_11* updates
    if t >= 0.0 and key_resp_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_11.tStart = t
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_11.status == STARTED:
        theseKeys = event.getKeys(keyList=['s'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in start_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start_2"-------
for thisComponent in start_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "start_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blank_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('blank.csv'),
    seed=None, name='blank_loop')
thisExp.addLoop(blank_loop)  # add the loop to the experiment
thisBlank_loop = blank_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlank_loop.rgb)
if thisBlank_loop != None:
    for paramName in thisBlank_loop:
        exec('{} = thisBlank_loop[paramName]'.format(paramName))

for thisBlank_loop in blank_loop:
    currentLoop = blank_loop
    # abbreviate parameter names if possible (e.g. rgb = thisBlank_loop.rgb)
    if thisBlank_loop != None:
        for paramName in thisBlank_loop:
            exec('{} = thisBlank_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "blank"-------
    t = 0
    blankClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    polygon.setPos([x, y])
    key_resp_7 = event.BuilderKeyResponse()
    # keep track of which components have finished
    blankComponents = [polygon, key_resp_7]
    for thisComponent in blankComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blankClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if t >= 0.0 and polygon.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon.tStart = t
            polygon.frameNStart = frameN  # exact frame index
            polygon.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if polygon.status == STARTED and t >= frameRemains:
            polygon.setAutoDraw(False)
        
        # *key_resp_7* updates
        if t >= 0.0 and key_resp_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_7.tStart = t
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_7.status == STARTED and t >= frameRemains:
            key_resp_7.status = FINISHED
        if key_resp_7.status == STARTED:
            theseKeys = event.getKeys(keyList=['c', 'b'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if key_resp_7.keys == []:  # then this was the first keypress
                    key_resp_7.keys = theseKeys[0]  # just the first key pressed
                    key_resp_7.rt = key_resp_7.clock.getTime()
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank"-------
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_7.keys in ['', [], None]:  # No response was made
        key_resp_7.keys=None
    blank_loop.addData('key_resp_7.keys',key_resp_7.keys)
    if key_resp_7.keys != None:  # we had a response
        blank_loop.addData('key_resp_7.rt', key_resp_7.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'blank_loop'


# set up handler to look after randomisation of conditions etc
scrambled_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('scrambled.csv'),
    seed=None, name='scrambled_loop')
thisExp.addLoop(scrambled_loop)  # add the loop to the experiment
thisScrambled_loop = scrambled_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisScrambled_loop.rgb)
if thisScrambled_loop != None:
    for paramName in thisScrambled_loop:
        exec('{} = thisScrambled_loop[paramName]'.format(paramName))

for thisScrambled_loop in scrambled_loop:
    currentLoop = scrambled_loop
    # abbreviate parameter names if possible (e.g. rgb = thisScrambled_loop.rgb)
    if thisScrambled_loop != None:
        for paramName in thisScrambled_loop:
            exec('{} = thisScrambled_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "scrambled"-------
    t = 0
    scrambledClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    image_5.setImage(stimulus)
    key_resp_6 = event.BuilderKeyResponse()
    # keep track of which components have finished
    scrambledComponents = [image_5, key_resp_6]
    for thisComponent in scrambledComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "scrambled"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = scrambledClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_5* updates
        if t >= 0.0 and image_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_5.tStart = t
            image_5.frameNStart = frameN  # exact frame index
            image_5.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_5.status == STARTED and t >= frameRemains:
            image_5.setAutoDraw(False)
        
        # *key_resp_6* updates
        if t >= 0.0 and key_resp_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_6.tStart = t
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_6.status == STARTED and t >= frameRemains:
            key_resp_6.status = FINISHED
        if key_resp_6.status == STARTED:
            theseKeys = event.getKeys(keyList=['c', 'b'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if key_resp_6.keys == []:  # then this was the first keypress
                    key_resp_6.keys = theseKeys[0]  # just the first key pressed
                    key_resp_6.rt = key_resp_6.clock.getTime()
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in scrambledComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "scrambled"-------
    for thisComponent in scrambledComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys=None
    scrambled_loop.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        scrambled_loop.addData('key_resp_6.rt', key_resp_6.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'scrambled_loop'


# set up handler to look after randomisation of conditions etc
happy_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('happy.csv'),
    seed=None, name='happy_loop')
thisExp.addLoop(happy_loop)  # add the loop to the experiment
thisHappy_loop = happy_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisHappy_loop.rgb)
if thisHappy_loop != None:
    for paramName in thisHappy_loop:
        exec('{} = thisHappy_loop[paramName]'.format(paramName))

for thisHappy_loop in happy_loop:
    currentLoop = happy_loop
    # abbreviate parameter names if possible (e.g. rgb = thisHappy_loop.rgb)
    if thisHappy_loop != None:
        for paramName in thisHappy_loop:
            exec('{} = thisHappy_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "happy"-------
    t = 0
    happyClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    image.setImage(stimulus)
    key_resp_2 = event.BuilderKeyResponse()
    # keep track of which components have finished
    happyComponents = [image, key_resp_2]
    for thisComponent in happyComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "happy"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = happyClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
        
        # *key_resp_2* updates
        if t >= 0.0 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_2.status == STARTED and t >= frameRemains:
            key_resp_2.status = FINISHED
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['b', 'c'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if key_resp_2.keys == []:  # then this was the first keypress
                    key_resp_2.keys = theseKeys[0]  # just the first key pressed
                    key_resp_2.rt = key_resp_2.clock.getTime()
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in happyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "happy"-------
    for thisComponent in happyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys=None
    happy_loop.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        happy_loop.addData('key_resp_2.rt', key_resp_2.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'happy_loop'


# set up handler to look after randomisation of conditions etc
sad_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('sad.csv'),
    seed=None, name='sad_loop')
thisExp.addLoop(sad_loop)  # add the loop to the experiment
thisSad_loop = sad_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSad_loop.rgb)
if thisSad_loop != None:
    for paramName in thisSad_loop:
        exec('{} = thisSad_loop[paramName]'.format(paramName))

for thisSad_loop in sad_loop:
    currentLoop = sad_loop
    # abbreviate parameter names if possible (e.g. rgb = thisSad_loop.rgb)
    if thisSad_loop != None:
        for paramName in thisSad_loop:
            exec('{} = thisSad_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "sad"-------
    t = 0
    sadClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    image_2.setImage(stimulus)
    key_resp_3 = event.BuilderKeyResponse()
    # keep track of which components have finished
    sadComponents = [image_2, key_resp_3]
    for thisComponent in sadComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "sad"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = sadClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_2* updates
        if t >= 0.0 and image_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_2.tStart = t
            image_2.frameNStart = frameN  # exact frame index
            image_2.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_2.status == STARTED and t >= frameRemains:
            image_2.setAutoDraw(False)
        
        # *key_resp_3* updates
        if t >= 0.0 and key_resp_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_3.tStart = t
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_3.status == STARTED and t >= frameRemains:
            key_resp_3.status = FINISHED
        if key_resp_3.status == STARTED:
            theseKeys = event.getKeys(keyList=['c', 'd'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if key_resp_3.keys == []:  # then this was the first keypress
                    key_resp_3.keys = theseKeys[0]  # just the first key pressed
                    key_resp_3.rt = key_resp_3.clock.getTime()
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sadComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "sad"-------
    for thisComponent in sadComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys=None
    sad_loop.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        sad_loop.addData('key_resp_3.rt', key_resp_3.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'sad_loop'


# set up handler to look after randomisation of conditions etc
angry_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('angry.csv'),
    seed=None, name='angry_loop')
thisExp.addLoop(angry_loop)  # add the loop to the experiment
thisAngry_loop = angry_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisAngry_loop.rgb)
if thisAngry_loop != None:
    for paramName in thisAngry_loop:
        exec('{} = thisAngry_loop[paramName]'.format(paramName))

for thisAngry_loop in angry_loop:
    currentLoop = angry_loop
    # abbreviate parameter names if possible (e.g. rgb = thisAngry_loop.rgb)
    if thisAngry_loop != None:
        for paramName in thisAngry_loop:
            exec('{} = thisAngry_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "angry"-------
    t = 0
    angryClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    image_3.setImage(stimulus)
    key_resp_4 = event.BuilderKeyResponse()
    # keep track of which components have finished
    angryComponents = [image_3, key_resp_4]
    for thisComponent in angryComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "angry"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = angryClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_3* updates
        if t >= 0.0 and image_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_3.tStart = t
            image_3.frameNStart = frameN  # exact frame index
            image_3.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_3.status == STARTED and t >= frameRemains:
            image_3.setAutoDraw(False)
        
        # *key_resp_4* updates
        if t >= 0.0 and key_resp_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_4.tStart = t
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_4.status == STARTED and t >= frameRemains:
            key_resp_4.status = FINISHED
        if key_resp_4.status == STARTED:
            theseKeys = event.getKeys(keyList=['b', 'c'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if key_resp_4.keys == []:  # then this was the first keypress
                    key_resp_4.keys = theseKeys[0]  # just the first key pressed
                    key_resp_4.rt = key_resp_4.clock.getTime()
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in angryComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "angry"-------
    for thisComponent in angryComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys=None
    angry_loop.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        angry_loop.addData('key_resp_4.rt', key_resp_4.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'angry_loop'


# set up handler to look after randomisation of conditions etc
neutral_loop = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('neutral.csv'),
    seed=None, name='neutral_loop')
thisExp.addLoop(neutral_loop)  # add the loop to the experiment
thisNeutral_loop = neutral_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNeutral_loop.rgb)
if thisNeutral_loop != None:
    for paramName in thisNeutral_loop:
        exec('{} = thisNeutral_loop[paramName]'.format(paramName))

for thisNeutral_loop in neutral_loop:
    currentLoop = neutral_loop
    # abbreviate parameter names if possible (e.g. rgb = thisNeutral_loop.rgb)
    if thisNeutral_loop != None:
        for paramName in thisNeutral_loop:
            exec('{} = thisNeutral_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "neutral"-------
    t = 0
    neutralClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    image_4.setImage(stimulus)
    key_resp_5 = event.BuilderKeyResponse()
    # keep track of which components have finished
    neutralComponents = [image_4, key_resp_5]
    for thisComponent in neutralComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "neutral"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = neutralClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_4* updates
        if t >= 0.0 and image_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_4.tStart = t
            image_4.frameNStart = frameN  # exact frame index
            image_4.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_4.status == STARTED and t >= frameRemains:
            image_4.setAutoDraw(False)
        
        # *key_resp_5* updates
        if t >= 0.0 and key_resp_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_5.tStart = t
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_5.status == STARTED and t >= frameRemains:
            key_resp_5.status = FINISHED
        if key_resp_5.status == STARTED:
            theseKeys = event.getKeys(keyList=['c', 'b'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if key_resp_5.keys == []:  # then this was the first keypress
                    key_resp_5.keys = theseKeys[0]  # just the first key pressed
                    key_resp_5.rt = key_resp_5.clock.getTime()
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in neutralComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "neutral"-------
    for thisComponent in neutralComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys=None
    neutral_loop.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        neutral_loop.addData('key_resp_5.rt', key_resp_5.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'neutral_loop'


# set up handler to look after randomisation of conditions etc
happy_loop2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('happy.csv'),
    seed=None, name='happy_loop2')
thisExp.addLoop(happy_loop2)  # add the loop to the experiment
thisHappy_loop2 = happy_loop2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisHappy_loop2.rgb)
if thisHappy_loop2 != None:
    for paramName in thisHappy_loop2:
        exec('{} = thisHappy_loop2[paramName]'.format(paramName))

for thisHappy_loop2 in happy_loop2:
    currentLoop = happy_loop2
    # abbreviate parameter names if possible (e.g. rgb = thisHappy_loop2.rgb)
    if thisHappy_loop2 != None:
        for paramName in thisHappy_loop2:
            exec('{} = thisHappy_loop2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "happy"-------
    t = 0
    happyClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    image.setImage(stimulus)
    key_resp_2 = event.BuilderKeyResponse()
    # keep track of which components have finished
    happyComponents = [image, key_resp_2]
    for thisComponent in happyComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "happy"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = happyClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
        
        # *key_resp_2* updates
        if t >= 0.0 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_2.status == STARTED and t >= frameRemains:
            key_resp_2.status = FINISHED
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['b', 'c'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if key_resp_2.keys == []:  # then this was the first keypress
                    key_resp_2.keys = theseKeys[0]  # just the first key pressed
                    key_resp_2.rt = key_resp_2.clock.getTime()
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in happyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "happy"-------
    for thisComponent in happyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys=None
    happy_loop2.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        happy_loop2.addData('key_resp_2.rt', key_resp_2.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'happy_loop2'


# set up handler to look after randomisation of conditions etc
sad_loop2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('sad.csv'),
    seed=None, name='sad_loop2')
thisExp.addLoop(sad_loop2)  # add the loop to the experiment
thisSad_loop2 = sad_loop2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSad_loop2.rgb)
if thisSad_loop2 != None:
    for paramName in thisSad_loop2:
        exec('{} = thisSad_loop2[paramName]'.format(paramName))

for thisSad_loop2 in sad_loop2:
    currentLoop = sad_loop2
    # abbreviate parameter names if possible (e.g. rgb = thisSad_loop2.rgb)
    if thisSad_loop2 != None:
        for paramName in thisSad_loop2:
            exec('{} = thisSad_loop2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "sad"-------
    t = 0
    sadClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    image_2.setImage(stimulus)
    key_resp_3 = event.BuilderKeyResponse()
    # keep track of which components have finished
    sadComponents = [image_2, key_resp_3]
    for thisComponent in sadComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "sad"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = sadClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_2* updates
        if t >= 0.0 and image_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_2.tStart = t
            image_2.frameNStart = frameN  # exact frame index
            image_2.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_2.status == STARTED and t >= frameRemains:
            image_2.setAutoDraw(False)
        
        # *key_resp_3* updates
        if t >= 0.0 and key_resp_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_3.tStart = t
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_3.status == STARTED and t >= frameRemains:
            key_resp_3.status = FINISHED
        if key_resp_3.status == STARTED:
            theseKeys = event.getKeys(keyList=['c', 'd'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if key_resp_3.keys == []:  # then this was the first keypress
                    key_resp_3.keys = theseKeys[0]  # just the first key pressed
                    key_resp_3.rt = key_resp_3.clock.getTime()
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sadComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "sad"-------
    for thisComponent in sadComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys=None
    sad_loop2.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        sad_loop2.addData('key_resp_3.rt', key_resp_3.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'sad_loop2'


# set up handler to look after randomisation of conditions etc
angry_loop2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('angry.csv'),
    seed=None, name='angry_loop2')
thisExp.addLoop(angry_loop2)  # add the loop to the experiment
thisAngry_loop2 = angry_loop2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisAngry_loop2.rgb)
if thisAngry_loop2 != None:
    for paramName in thisAngry_loop2:
        exec('{} = thisAngry_loop2[paramName]'.format(paramName))

for thisAngry_loop2 in angry_loop2:
    currentLoop = angry_loop2
    # abbreviate parameter names if possible (e.g. rgb = thisAngry_loop2.rgb)
    if thisAngry_loop2 != None:
        for paramName in thisAngry_loop2:
            exec('{} = thisAngry_loop2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "angry"-------
    t = 0
    angryClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    image_3.setImage(stimulus)
    key_resp_4 = event.BuilderKeyResponse()
    # keep track of which components have finished
    angryComponents = [image_3, key_resp_4]
    for thisComponent in angryComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "angry"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = angryClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_3* updates
        if t >= 0.0 and image_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_3.tStart = t
            image_3.frameNStart = frameN  # exact frame index
            image_3.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_3.status == STARTED and t >= frameRemains:
            image_3.setAutoDraw(False)
        
        # *key_resp_4* updates
        if t >= 0.0 and key_resp_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_4.tStart = t
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_4.status == STARTED and t >= frameRemains:
            key_resp_4.status = FINISHED
        if key_resp_4.status == STARTED:
            theseKeys = event.getKeys(keyList=['b', 'c'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if key_resp_4.keys == []:  # then this was the first keypress
                    key_resp_4.keys = theseKeys[0]  # just the first key pressed
                    key_resp_4.rt = key_resp_4.clock.getTime()
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in angryComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "angry"-------
    for thisComponent in angryComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys=None
    angry_loop2.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        angry_loop2.addData('key_resp_4.rt', key_resp_4.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'angry_loop2'


# set up handler to look after randomisation of conditions etc
netral_2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('neutral.csv'),
    seed=None, name='netral_2')
thisExp.addLoop(netral_2)  # add the loop to the experiment
thisNetral_2 = netral_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNetral_2.rgb)
if thisNetral_2 != None:
    for paramName in thisNetral_2:
        exec('{} = thisNetral_2[paramName]'.format(paramName))

for thisNetral_2 in netral_2:
    currentLoop = netral_2
    # abbreviate parameter names if possible (e.g. rgb = thisNetral_2.rgb)
    if thisNetral_2 != None:
        for paramName in thisNetral_2:
            exec('{} = thisNetral_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "neutral"-------
    t = 0
    neutralClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    image_4.setImage(stimulus)
    key_resp_5 = event.BuilderKeyResponse()
    # keep track of which components have finished
    neutralComponents = [image_4, key_resp_5]
    for thisComponent in neutralComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "neutral"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = neutralClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_4* updates
        if t >= 0.0 and image_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_4.tStart = t
            image_4.frameNStart = frameN  # exact frame index
            image_4.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_4.status == STARTED and t >= frameRemains:
            image_4.setAutoDraw(False)
        
        # *key_resp_5* updates
        if t >= 0.0 and key_resp_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_5.tStart = t
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_5.status == STARTED and t >= frameRemains:
            key_resp_5.status = FINISHED
        if key_resp_5.status == STARTED:
            theseKeys = event.getKeys(keyList=['c', 'b'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if key_resp_5.keys == []:  # then this was the first keypress
                    key_resp_5.keys = theseKeys[0]  # just the first key pressed
                    key_resp_5.rt = key_resp_5.clock.getTime()
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in neutralComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "neutral"-------
    for thisComponent in neutralComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys=None
    netral_2.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        netral_2.addData('key_resp_5.rt', key_resp_5.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'netral_2'


# set up handler to look after randomisation of conditions etc
scrambled_loop2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('scrambled.csv'),
    seed=None, name='scrambled_loop2')
thisExp.addLoop(scrambled_loop2)  # add the loop to the experiment
thisScrambled_loop2 = scrambled_loop2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisScrambled_loop2.rgb)
if thisScrambled_loop2 != None:
    for paramName in thisScrambled_loop2:
        exec('{} = thisScrambled_loop2[paramName]'.format(paramName))

for thisScrambled_loop2 in scrambled_loop2:
    currentLoop = scrambled_loop2
    # abbreviate parameter names if possible (e.g. rgb = thisScrambled_loop2.rgb)
    if thisScrambled_loop2 != None:
        for paramName in thisScrambled_loop2:
            exec('{} = thisScrambled_loop2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "scrambled"-------
    t = 0
    scrambledClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    image_5.setImage(stimulus)
    key_resp_6 = event.BuilderKeyResponse()
    # keep track of which components have finished
    scrambledComponents = [image_5, key_resp_6]
    for thisComponent in scrambledComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "scrambled"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = scrambledClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_5* updates
        if t >= 0.0 and image_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_5.tStart = t
            image_5.frameNStart = frameN  # exact frame index
            image_5.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_5.status == STARTED and t >= frameRemains:
            image_5.setAutoDraw(False)
        
        # *key_resp_6* updates
        if t >= 0.0 and key_resp_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_6.tStart = t
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_6.status == STARTED and t >= frameRemains:
            key_resp_6.status = FINISHED
        if key_resp_6.status == STARTED:
            theseKeys = event.getKeys(keyList=['c', 'b'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if key_resp_6.keys == []:  # then this was the first keypress
                    key_resp_6.keys = theseKeys[0]  # just the first key pressed
                    key_resp_6.rt = key_resp_6.clock.getTime()
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in scrambledComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "scrambled"-------
    for thisComponent in scrambledComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys=None
    scrambled_loop2.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        scrambled_loop2.addData('key_resp_6.rt', key_resp_6.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'scrambled_loop2'


# set up handler to look after randomisation of conditions etc
blank_loop2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('blank.csv'),
    seed=None, name='blank_loop2')
thisExp.addLoop(blank_loop2)  # add the loop to the experiment
thisBlank_loop2 = blank_loop2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlank_loop2.rgb)
if thisBlank_loop2 != None:
    for paramName in thisBlank_loop2:
        exec('{} = thisBlank_loop2[paramName]'.format(paramName))

for thisBlank_loop2 in blank_loop2:
    currentLoop = blank_loop2
    # abbreviate parameter names if possible (e.g. rgb = thisBlank_loop2.rgb)
    if thisBlank_loop2 != None:
        for paramName in thisBlank_loop2:
            exec('{} = thisBlank_loop2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "blank"-------
    t = 0
    blankClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    polygon.setPos([x, y])
    key_resp_7 = event.BuilderKeyResponse()
    # keep track of which components have finished
    blankComponents = [polygon, key_resp_7]
    for thisComponent in blankComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blankClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if t >= 0.0 and polygon.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon.tStart = t
            polygon.frameNStart = frameN  # exact frame index
            polygon.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if polygon.status == STARTED and t >= frameRemains:
            polygon.setAutoDraw(False)
        
        # *key_resp_7* updates
        if t >= 0.0 and key_resp_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_7.tStart = t
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_7.status == STARTED and t >= frameRemains:
            key_resp_7.status = FINISHED
        if key_resp_7.status == STARTED:
            theseKeys = event.getKeys(keyList=['c', 'b'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if key_resp_7.keys == []:  # then this was the first keypress
                    key_resp_7.keys = theseKeys[0]  # just the first key pressed
                    key_resp_7.rt = key_resp_7.clock.getTime()
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank"-------
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_7.keys in ['', [], None]:  # No response was made
        key_resp_7.keys=None
    blank_loop2.addData('key_resp_7.keys',key_resp_7.keys)
    if key_resp_7.keys != None:  # we had a response
        blank_loop2.addData('key_resp_7.rt', key_resp_7.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'blank_loop2'


# ------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [polygon_2]
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_2* updates
    if t >= 0.0 and polygon_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_2.tStart = t
        polygon_2.frameNStart = frameN  # exact frame index
        polygon_2.setAutoDraw(True)
    frameRemains = 0.0 + 10- win.monitorFramePeriod * 0.75  # most of one frame period left
    if polygon_2.status == STARTED and t >= frameRemains:
        polygon_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
