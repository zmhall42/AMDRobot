# This is to test both motors and PWM setup using classes and functions.  The class and 
# dependent functions created here can be used to set up the motors in other bits of code.
#
# 2021-04-23
# Written by: The Autonomous Metal Detector Robot capstone group at TnTech.
#
#	What to check on next test with the robot:
#	1. Check if Tank drive class works.
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

class Tank:
	def __init__(self, left, right):
		self.left = left
		self.right = right
	def setup(self):
		pass
	def forward(self, duty_cycle):
		self.left.forward(duty_cycle)
		self.right.forward(duty_cycle)
	def reverse(self, duty_cycle):
		self.left.reverse(duty_cycle)
		self.right.reverse(duty_cycle)
	def stop(self):
		self.left.stop()
		self.right.stop()
	
		
		
#----------------------------------Global Variables--------------------------------------
#Left Side
ml_pwm_pin = 32	#GPIO 12 PWM for M1
ml_dir_pin = 29	#GPIO 5 DIR for M1
ml_clock_f = 1000	#PWM clock set to 1 kHz
ml_reversed = True;	#True if reversed, False if normal rotation
#Right Side
mr_pwm_pin = 12 #GPIO 18 PWM for M2 - Left SIde
mr_dir_pin = 36	#GPIO 16 DIR for M2
mr_clock_f = 1000	#PWM clock set to 1 kHz
mr_reversed = False;	#True if reversed, False if normal rotation



#------------------------------Create and Setup Objects----------------------------------
MR = Motor(mr_pwm_pin, mr_dir_pin, mr_clock_f, mr_reversed)
MR.setup()
ML = Motor(ml_pwm_pin, ml_dir_pin, ml_clock_f, ml_reversed)
ML.setup()

Robot = Tank(ML, MR)
Robot.setup()



#-------------------------------------Program Body---------------------------------------
Robot.forward(25)						#goes forward
throw_away_val = input("Enter some char and press enter to change directions: ")	#reverses direction
Robot.reverse(25)						#goes in reverse
throw_away_val = input("Enter some char and press enter to stop: ")	#stops the robot
Robot.stop()						#stops tank
GPIO.cleanup()						#used to clean up anything the GPIO library creates