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



#-------------------------------------Libraries------------------------------------------
import RPi.GPIO as GPIO		#include the GPIO library
GPIO.setmode(GPIO.BOARD)	#use physical layout numbering system
import curses				#include the curses read keyboard ascii library

GPIO.setwarnings(False)		#turns off warning messages



#---------------------------------Class Definitions--------------------------------------
#never include anything in the motor position of the class/function calls (ex. use motor_name.setup(), NOT motor_name.setup(variable) because motor is ignored)
class Motor:
	def __init__(motor, pwm_pin, direction_pin, clock_frequency, reversed):
		motor.pwm_pin = pwm_pin
		motor.direction_pin = direction_pin
		motor.clock_frequency = clock_frequency
		motor.reversed = reversed
	def setup(motor):								#run either this or set up both sides at the same time with tank function
		GPIO.setup(motor.pwm_pin, GPIO.OUT)
		GPIO.setup(motor.direction_pin, GPIO.OUT)
		motor.m_pwm = GPIO.PWM(motor.pwm_pin, motor.clock_frequency)
		motor.m_pwm.start(0)							#start at 0 duty cycle
	def forward(motor, speed):
		if motor.reversed == True:					#check if reversed and set correct direction
			GPIO.output(motor.direction_pin, GPIO.HIGH)
		else:
			GPIO.output(motor.direction_pin, GPIO.LOW)
		motor.m_pwm.ChangeDutyCycle(speed)			#restart at new speed
	def reverse(motor, speed):
		if motor.reversed == True:					#check if reversed and set correct direction
			GPIO.output(motor.direction_pin, GPIO.LOW)
		else:
			GPIO.output(motor.direction_pin, GPIO.HIGH)
		motor.m_pwm.ChangeDutyCycle(speed)			#restart at new speed
	def stop(motor):
		motor.m_pwm.ChangeDutyCycle(0)				#stop
	def cleanup(motor):
		motor.m_pwm.stop()

#never include anything in the tank position of the class/function calls (ex. use motor_name.setup(), NOT motor_name.setup(variable) because tank is ignored)
class Tank:
	def __init__(tank, left, right):
		tank.left = left
		tank.right = right
	def setup(tank):								#run either this or set up both sides manually
		tank.left.setup()
		tank.right.setup()
	def forward(tank, duty_cycle):
		tank.left.forward(duty_cycle)
		tank.right.forward(duty_cycle)
	def reverse(tank, duty_cycle):
		tank.left.reverse(duty_cycle)
		tank.right.reverse(duty_cycle)
	def left_on_axis(tank, duty_cycle):				#spin to the left on center axis
		tank.left.reverse(duty_cycle)
		tank.right.forward(duty_cycle)
	def left(tank, duty_cycle):						#spin around left track
		tank.left.stop()
		tank.right.forward(duty_cycle)
	def right_on_axis(tank, duty_cycle):			#spin to the right on center axis
		tank.left.forward(duty_cycle)
		tank.right.reverse(duty_cycle)
	def right(tank, duty_cycle):					#spin around left track
		tank.left.forward(duty_cycle)
		tank.right.stop()
	def stop(tank):
		tank.left.stop()
		tank.right.stop()
	def cleanup(tank):
		tank.left.cleanup()
		tank.right.cleanup()
	
		
		
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
	speed = 30
	while True:
		char = screen.getch()
		if char == ord('e'):
			break
		elif char == ord('w'):
			Robot.forward(speed)
		elif char == ord('s'):
			Robot.reverse(speed)
		elif char == ord('a'):
			Robot.left(speed)
		elif char == ord('d'):
			Robot.right(speed)
		elif char == ord('l'):
			Robot.left_on_axis(speed)
		elif char == ord('r'):
			Robot.right_on_axis(speed)
		else:
			Robot.stop()

finally:
	curses.nocbreak()
	screen.keypad(False)
	curses.echo()
	curses.endwin()
	Robot.cleanup()
	GPIO.cleanup()			#used to clean up anything the GPIO library creates