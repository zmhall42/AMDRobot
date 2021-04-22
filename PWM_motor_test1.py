#This is to test the motors and PWM setup
#
# 2021-04-22

import RPI.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32,GPIO.OUT)			#GPIO 12 PWM 0

soft_pwm = GPIO.PWM(32,1000)	#set PWM on pin 32 to 1 kHz PWM clock
soft_pwm.start(50)				#50% duty cycle
input("Press return to stop: ")
soft_pwm.stop()
GPIO.cleanup()