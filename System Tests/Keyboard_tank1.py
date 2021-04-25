# This uses keyboard inputs to drive the robot like a tank.
#
# 2021-04-23
# Written by: The Autonomous Metal Detector Robot capstone group at TnTech.
#
#	How to drive:
#		w: forward
#		s: reverse
#		a: turn left
#		d: turn right
#		l: turn left on center axis
#		r: turn right on center axis
#		e: stop the program
#
#	Error log:
#		2021-04-23_19:00	When running the code, w & s work fine, a or d breaks it.
#			The error on the terminal is this: AttributeError: Robot instance has no __call__ method
#			Not sure why.  Changed self attribute of Motor to motor and of Tank to tank.
#		2021-04-23_23:45	Found the problem.  There was a Tank.left which was the left 
# 			motor and Tank.left() which was turn the tank left.  A class cannot have an
#			attribute and a method named the same.  Reverted the motor and tank listed 
# 			above back to self and reset some variable names.  Implemented the motor name
#			changes in the Tank class.



#-------------------------------------Libraries------------------------------------------
import RPi.GPIO as GPIO		#include the GPIO library
GPIO.setmode(GPIO.BOARD)	#use physical layout numbering system
import curses				#include the curses read keyboard ascii library

GPIO.setwarnings(False)		#turns off warning messages



#---------------------------------Class Definitions--------------------------------------
#never include anything in the self position of the class/function calls (ex. use self_name.setup(), NOT self_name.setup(variable) because self is ignored)
class Motor:
	def __init__(self, pwm_pin, direction_pin, clock_frequency, reversed):
		self.pwm_pin = pwm_pin
		self.direction_pin = direction_pin
		self.clock_frequency = clock_frequency
		self.reversed = reversed
	def setup(self):								#run either this or set up both sides at the same time with tank function
		GPIO.setup(self.pwm_pin, GPIO.OUT)
		GPIO.setup(self.direction_pin, GPIO.OUT)
		self.m_pwm = GPIO.PWM(self.pwm_pin, self.clock_frequency)
		self.m_pwm.start(0)							#start at 0 duty cycle
	def forward(self, duty_cycle):
		if self.reversed == True:					#check if reversed and set correct direction
			GPIO.output(self.direction_pin, GPIO.HIGH)
		else:
			GPIO.output(self.direction_pin, GPIO.LOW)
		self.m_pwm.ChangeDutyCycle(duty_cycle)			#restart at new duty_cycle
	def reverse(self, duty_cycle):
		if self.reversed == True:					#check if reversed and set correct direction
			GPIO.output(self.direction_pin, GPIO.LOW)
		else:
			GPIO.output(self.direction_pin, GPIO.HIGH)
		self.m_pwm.ChangeDutyCycle(duty_cycle)			#restart at new duty_cycle
	def stop(self):
		self.m_pwm.ChangeDutyCycle(0)				#stop
	def cleanup(self):
		self.m_pwm.stop()

#never include anything in the self position of the class/function calls (ex. use self_name.setup(), NOT self_name.setup(variable) because self is ignored)
class Tank:
	def __init__(self, left, right):
		self.left_motor = left
		self.right_motor = right
	def setup(self):								#run either this or set up both sides manually
		self.left_motor.setup()
		self.right_motor.setup()
	def forward(self, duty_cycle):
		self.left_motor.forward(duty_cycle)
		self.right_motor.forward(duty_cycle)
	def reverse(self, duty_cycle):
		self.left_motor.reverse(duty_cycle)
		self.right_motor.reverse(duty_cycle)
	def left_on_axis(self, duty_cycle):				#spin to the left on center axis
		self.left_motor.reverse(duty_cycle)
		self.right_motor.forward(duty_cycle)
	def left(self, duty_cycle):						#spin around left track
		self.left_motor.stop()
		self.right_motor.forward(duty_cycle)
	def right_on_axis(self, duty_cycle):			#spin to the right on center axis
		self.left_motor.forward(duty_cycle)
		self.right_motor.reverse(duty_cycle)
	def right(self, duty_cycle):					#spin around right track
		self.left_motor.forward(duty_cycle)
		self.right_motor.stop()
	def stop(self):
		self.left_motor.stop()
		self.right_motor.stop()
	def cleanup(self):
		self.left_motor.cleanup()
		self.right_motor.cleanup()
	
		
		
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
ML = Motor(ml_pwm_pin, ml_dir_pin, ml_clock_f, ml_reversed)
Robot = Tank(ML, MR)
Robot.setup()

#set up curses screen
screen = curses.initscr()	#get the curses window
curses.noecho()				#turn of echoing the keyboard to the screen
curses.cbreak()				#turn on instant (no wait) key response
curses.halfdelay(3)			#
screen.keypad(True)			#use special values for cursor keys



#-------------------------------------Program Body---------------------------------------
try:
	duty_cycle = 30
	while True:
		char = screen.getch()
		if char == ord('e'):
			break
		elif char == ord('w'):
			Robot.forward(duty_cycle)
		elif char == ord('s'):
			Robot.reverse(duty_cycle)
		elif char == ord('a'):
			Robot.left(duty_cycle)
		elif char == ord('d'):
			Robot.right(duty_cycle)
		elif char == ord('l'):
			Robot.left_on_axis(duty_cycle)
		elif char == ord('r'):
			Robot.right_on_axis(duty_cycle)
		else:
			Robot.stop()

finally:
	curses.nocbreak()
	screen.keypad(False)
	curses.echo()
	curses.endwin()
	Robot.cleanup()
	GPIO.cleanup()			#used to clean up anything the GPIO library creates