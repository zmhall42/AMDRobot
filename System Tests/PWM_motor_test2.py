# This is to test both motors and PWM setup using classes and functions.  The class and 
# dependent functions created here can be used to set up the motors in other bits of code.
#
# 2021-04-23
# Written by: The Autonomous Metal Detector Robot capstone group at TnTech.
#
#	What to check on next test with the robot:
#	1. Check that the class works with init and setup by running the code as is. ***DONE, works fine.
#	2. Test that the body code works by running the code as is.	***DONE, works fine.
#	3. Run and get the correct directions for ML and MR in the globals through trial and 
#		error.	***Done, was wrong to start but the directions are now set correctly.
#	4. Try commented code in the class definition and getting the correct directions for 
#		forward and reverse.	***DONE, works fine.
#	5. If the class code works, try commenting out the code in the body and and uncomment 
#		the code after it.	***DONE, works fine.
#edit


#-------------------------------------Libraries------------------------------------------
import RPi.GPIO as GPIO		#include the GPIO library
GPIO.setmode(GPIO.BOARD)	#use physical layout numbering system



#---------------------------------Class Definitions--------------------------------------
class Motor:
	def __init__(self, pwm_pin, direction_pin, clock_frequency, reversed):
		self.pwm_pin = pwm_pin
		self.direction_pin = direction_pin
		self.clock_frequency = clock_frequency
		self.reversed = reversed
	def setup(self):
		GPIO.setup(self.pwm_pin, GPIO.OUT)
		GPIO.setup(self.direction_pin, GPIO.OUT)
		self.m_pwm = GPIO.PWM(self.pwm_pin, self.clock_frequency)
	def forward(self, speed):
		self.m_pwm.stop()							#stop
		if self.reversed == True:					#check if reversed and set correct direction
			GPIO.output(self.direction_pin, GPIO.HIGH)
		else:
			GPIO.output(self.direction_pin, GPIO.LOW)
		self.m_pwm.start(speed)						#restart at new speed
	def reverse(self, speed):
		self.m_pwm.stop()							#stop
		if self.reversed == True:					#check if reversed and set correct direction
			GPIO.output(self.direction_pin, GPIO.LOW)
		else:
			GPIO.output(self.direction_pin, GPIO.HIGH)
		self.m_pwm.start(speed)						#restart at new speed
	def stop(self):
		self.m_pwm.stop()							#stop
	
		
		
#----------------------------------Global Variables--------------------------------------
#Right Side
mr_pwm_pin = 32	#GPIO 12 PWM for M1
mr_dir_pin = 29	#GPIO 5 DIR for M1
mr_clock_f = 1000	#PWM clock set to 1 kHz
mr_reversed = True;	#True if reversed, False if normal rotation
#Left Side
ml_pwm_pin = 12 #GPIO 18 PWM for M2 - Left SIde
ml_dir_pin = 36	#GPIO 16 DIR for M2
ml_clock_f = 1000	#PWM clock set to 1 kHz
ml_reversed = False;	#True if reversed, False if normal rotation




#------------------------------Create and Setup Objects----------------------------------
MR = Motor(mr_pwm_pin, mr_dir_pin, mr_clock_f, mr_reversed)
MR.setup()
ML = Motor(ml_pwm_pin, ml_dir_pin, ml_clock_f, ml_reversed)
ML.setup()



#-------------------------------------Program Body---------------------------------------
MR.forward(25)						#goes forward
ML.forward(25)
throw_away_val = input("Enter some char and press enter to change directions: ")	#reverses direction
MR.reverse(25)						#goes in reverse
ML.reverse(25)
throw_away_val = input("Enter some char and press enter to stop: ")	#stops the robot
MR.stop()							#stops mr motor
ML.stop()
GPIO.cleanup()						#used to clean up anything the GPIO library creates