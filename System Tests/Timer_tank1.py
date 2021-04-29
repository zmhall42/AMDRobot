# This uses timers to drive the robot like a tank.  It follows a predefined path taped 
# on the floor of the Capstone lab.
#
# 2021-04-29
# Written by: The Autonomous Metal Detector Robot capstone group at TnTech.



#-------------------------------------Libraries------------------------------------------
import RPi.GPIO as GPIO		#include the GPIO library
GPIO.setmode(GPIO.BOARD)	#use physical layout numbering system

from time import sleep      #import the sleep function from the time library

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
		self.m_pwm.ChangeDutyCycle(duty_cycle)		#restart at new duty_cycle
	def reverse(self, duty_cycle):
		if self.reversed == True:					#check if reversed and set correct direction
			GPIO.output(self.direction_pin, GPIO.LOW)
		else:
			GPIO.output(self.direction_pin, GPIO.HIGH)
		self.m_pwm.ChangeDutyCycle(duty_cycle)		#restart at new duty_cycle
	def stop(self):
		self.m_pwm.ChangeDutyCycle(0)				#stop
	def cleanup(self):
		self.m_pwm.stop()

#never include anything in the self position of the class/function calls (ex. use self_name.setup(), NOT self_name.setup(variable) because self is ignored)
class Tank:
	def __init__(self, left, right, left_trim = 0, right_trim = 0):
		self.left_motor = left
		self.right_motor = right
        self.left_trim = left_trim
        self.right_trim = right_trim
	def setup(self):								#run either this or set up both sides manually
		self.left_motor.setup()
		self.right_motor.setup()
    def trim(self, left, right):
        self.left_trim = left
        self.right_trim = right
	def forward(self, duty_cycle):
		self.left_motor.forward(duty_cycle + self.left_trim)
		self.right_motor.forward(duty_cycle + self.right_trim)
	def reverse(self, duty_cycle):
		self.left_motor.reverse(duty_cycle + self.left_trim)
		self.right_motor.reverse(duty_cycle + self.right_trim)
	def left_on_axis(self, duty_cycle):				#spin to the left on center axis
		self.left_motor.reverse(duty_cycle + self.left_trim)
		self.right_motor.forward(duty_cycle + self.right_trim)
	def left(self, duty_cycle):						#spin around left track
		self.left_motor.stop()
		self.right_motor.forward(duty_cycle + self.right_trim)
	def right_on_axis(self, duty_cycle):			#spin to the right on center axis
		self.left_motor.forward(duty_cycle + self.left_trim)
		self.right_motor.reverse(duty_cycle + self.right_trim)
	def right(self, duty_cycle):					#spin around right track
		self.left_motor.forward(duty_cycle  + self.left_trim)
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

speed = 25
Robot.forward(speed)
sleep(9.300)
Robot.stop()
sleep(0.500)
Robot.left_on_axis(speed)
sleep(0.880)
Robot.stop()
sleep(0.500)
#Robot.forward(speed)
#sleep(2.000)
#Robot.stop()
#sleep(0.500)
#Robot.left_on_axis(speed)
#sleep(3.250)
#Robot.stop()
#sleep(0.500)
#Robot.forward(speed)
#sleep(2.000)
#Robot.stop()
#Robot.right_on_axis(speed)
#sleep(0.880)
#Robot.stop()
#sleep(0.500)
#Robot.forward(speed)
#sleep(9.300)
#Robot.stop()


# Cleanup code
Robot.cleanup()
GPIO.cleanup()			#used to clean up anything the GPIO library creates