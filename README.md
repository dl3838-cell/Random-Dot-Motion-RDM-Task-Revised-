# Random-Dot-Motion-RDM-Task-Revised-
Overview

This experiment implements a Random Dot Motion (RDM) task, also known as a Random Dot Kinematogram (RDK), designed to measure motion perception thresholds and decision-making processes. Participants view a circular field of moving dots and must judge the overall direction of coherent motion (up or down) while varying levels of noise are present.

Task Description

What Participants See

A circular aperture containing 150 white dots on a black background Some dots move coherently in one direction (signal dots) Other dots move randomly (noise dots) Participants must identify whether the coherent motion is upward or downward

Trial Structure

Fixation Cross (0.5-1.5 seconds): Participants focus on a central fixation point Motion Stimulus: Dots appear and continue moving until a response is made Response: Participants press arrow keys to indicate perceived direction Inter-trial Interval (0.5 seconds): Brief blank screen before next trial

Experimental Design

Motion Coherence: 5 levels (5%, 10%, 20%, 40%, 80%)

Lower coherence = harder to detect motion direction Higher coherence = easier to detect motion direction

Motion Direction: 2 levels (90° = upward, 270° = downward)

Dependent Variables

Accuracy: Whether response matches actual motion direction Reaction Time (RT): Time from stimulus onset to response

Trial Count - User Defined

In experiment info box the user enters the trial information The code will generate a set of trials containing an equal number of coherence and direction settings Trials are randomly ordered to prevent anticipation effects

Stimulus Parameters

Number of dots = 150 Dot size = 5 pixels Dot speed = 0.5°/frame

Response Instructions

UP Arrow: Indicate upwardward motion DOWN Arrow: Indicate downward motion ESC: Exit experiment (emergency exit)

Participants should respond as quickly and accurately as possible once they perceive the motion direction.

Output Data

The experiment saves two files with timestamp:

Excel file (participantID_random_dot_motion.xlsx)

Data Columns

coherence: Motion coherence level for that trial direction: Actual motion direction (90 or 270) correct_response: Expected response ('up' or 'down') response: Participant's actual response rt: Reaction time in seconds correct: Boolean indicating if response was correct fixation_duration: Duration of fixation period
