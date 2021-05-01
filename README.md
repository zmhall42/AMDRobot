# AMDRobot
Autonomous Metal Detector Robot (Spring 2021 - Fall 2021 senior capstone project) at Tennessee Technological University.  
This group consists of an EE and ME team.

About:
This repository will hold all of the code to be run on the Raspberry Pi 4 B+.  All code will be saved here with local 
copies saved often for redundancy.  If anyone has any questions, direct them to Z Hall (EE).  This repo is open to edits 
from both ME and EE teams.  

How to use:
Edit on your computer, push to Github, and pull on the Pi.  Push updates often to prevent others from overwriting your 
code or from creating overlapping changes.  (There is a feature to make this not so bad, but it's difficult to revert
these changes if it happens.)

***Please comment your changes well in the update and description blank.  Failure to do so will cause headaches.  It will 
take more time to troubleshoot poorly commented code than to write efficient comments.***

# Programs by Folder
***Unless otherwise stated, emergency exit the programs by pressing CTRL+C on the input device.***

System Tests:
  - Keyboard_tank1.py:  Allows the user to drive the robot via the input device (i.e. computer if ssh-ing into the pi or 
                        a keyboard if pugged directly into the pi via USB.  To drive the robot, use W,A,S and D to go 
                        forward, left, backwards and right (respectively).  To do a center axis turn, press L to go to 
                        the left or r to go to the right.  When you want to terminate the program and return to the 
                        terminal, press E.
  - PWM_motor_test1.py: This runs both drive motors forward at 25% speed.  There is no user control, only to stop the 
                        program.  To stop, the screen says press return/enter, which you can do, but will cause an error 
                        or an exception.  Instead, type any character and hit enter to exit smoothly.
  - PWM_motor_test2.py: This is the same program as PWM_motor_test1.py, except for using classes to control the motors
                        (program side) and an added direction change.  After sending a character and presing enter the 
                        first time (same as the aformentioned program, the motors will change direction and go backwards 
                        with another prompt on-screen, this one for terminating the program.
  - PWM_tank_drive_test1.py:  This is the same operation and function as PWM_motor_test2.py, the only difference being 
                              using another class to control the motors labelled as tank (program side).
  - PWM_tank_drive_test2.py:  This is the same functionality as PWM_motor_test1.py, but uses both motor classes and tank 
                              classes created in PWM_tank_drive_test1.py.  This was created to troubleshoot some direction
                              issues found in PWM_motor_test1.py, PWM_motor_test2.py, and PWM_tank_drive_test1.py.  Those 
                              issues have been resolved and imlemented.
  - Timer_tank1.py: This program uses the classes and general code format as it was inspired by the PWM_tank_drive_tests.
                    This program "follows" a predefined path taped to the floor of the EE capstone lab. It goes 
                    approximately 10 feet forwards, does a 90-degree left turn, goes 4 feet forwards, does a 180-degree 
                    center axis left turn, goes forward 4 feet, turns right 90 degrees, and returns to the starting position 
                    by going 10 feet forwards.  The speed of the motors is set to 25%.  This program resulted in the left 
                    track continually popping off at random times and throwing off the timers off.
  - Timer_tank2.py: This program is identical to Timer_tank2.py, except it is run at half speed of 12.5%.  Consequently, the
                    timers are doubled to make up for running at half speed.  This code did not keep the track from popping 
                    off issue and was therefore not used.  This program was written on the Pi as a copy of Timer_tank1.py.
