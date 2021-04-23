#This is to test the motors and PWM setup
#
# 2021-04-22

import RPi.GPIO as GPIO

m1_pwm_pin = 32	#GPIO 12 PWM for M1
m1_dir_pin = 29	#GPIO 5 DIR for M1 
m2_pwm_pin = 12 #GPIO 18 PWM for M2
m2_dir_pin = 36	#GPIO 16 DIR for M2

GPIO.setmode(GPIO.BOARD)
GPIO.setup(m1_pwm_pin, GPIO.OUT)
GPIO.setup(m1_dir_pin, GPIO.OUT)
GPIO.setup(m2_pwm_pin, GPIO.OUT)
GPIO.setup(m2_dir_pin, GPIO.OUT)

GPIO.output(m1_dir_pin, GPIO.HIGH)	#set direction fwd = 1, rev = 0 
GPIO.output(m2_dir_pin, GPIO.LOW)
m1_pwm = GPIO.PWM(m1_pwm_pin, 1000)	#set PWM on pin 32 to 1 kHz PWM clock
m2_pwm = GPIO.PWM(m2_pwm_pin, 1000)
m1_pwm.start(25)			#25% duty cycle
m2_pwm.start(25)
input("Press return to stop: ")
m1_pwm.stop()
m2_pwm.stop()
GPIO.cleanup()
