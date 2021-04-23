#This is to test both motors and PWM setup.
#
# 2021-04-22
# Written by: The Autonomous Metal Detector Robot capstone group at TnTech.

#-------------------------------------Libraries------------------------------------------
import RPi.GPIO as GPIO		#include the GPIO library

#----------------------------------Global Variables--------------------------------------
m1_pwm_pin = 32	#GPIO 12 PWM for M1 - Right side
m1_dir_pin = 29	#GPIO 5 DIR for M1 
m2_pwm_pin = 12 #GPIO 18 PWM for M2 - Left SIde
m2_dir_pin = 36	#GPIO 16 DIR for M2

#-------------------------------------Pin Setup------------------------------------------
GPIO.setmode(GPIO.BOARD)	#set the pin numbering mode to the physical pins on the board
GPIO.setup(m1_pwm_pin, GPIO.OUT)	#set mode of the pins
GPIO.setup(m1_dir_pin, GPIO.OUT)
GPIO.setup(m2_pwm_pin, GPIO.OUT)
GPIO.setup(m2_dir_pin, GPIO.OUT)

#-------------------------------------Program Body---------------------------------------
GPIO.output(m1_dir_pin, GPIO.HIGH)	#set direction fwd = 1, rev = 0 
GPIO.output(m2_dir_pin, GPIO.LOW)
m1_pwm = GPIO.PWM(m1_pwm_pin, 1000)	#set PWM on m1_pwm_pin to 1 kHz PWM clock
m2_pwm = GPIO.PWM(m2_pwm_pin, 1000)
m1_pwm.start(25)					#25% duty cycle
m2_pwm.start(25)
input("Press return to stop: ")		#wait on terminal input of the enter/return key
m1_pwm.stop()						#stops m1 motor
m2_pwm.stop()
GPIO.cleanup()						#used to clean up anything the GPIO library creates