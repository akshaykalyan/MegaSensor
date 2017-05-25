import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)
class pp(object):
	"""Post Processing Mega sensor"""
	def __init__(self, arg=[])://Analog output calibration function
		self.arg = arg
		if self.arg[0]<=485:
			self.arg[0]=int(round(self.arg[0]/(48.5)-10))
		else :
			self.arg[0]=int(round(self.arg[0]/(53.8)-9))
		if self.arg[1]<=521:
			self.arg[1]=int(round(10-self.arg[1]/(52.1)))
		else :
			self.arg[1]=int(round(10-self.arg[1]/(50.2)))
		self.arg[2]=int(round(10-(arg[2]-31)/93))
		if self.arg[3]<520 or self.arg[3]>540:
			self.arg[3]=1
		else:
			self.arg[3]=0
		if self.arg[4]>1000:
                        self.arg[4]=1
                else:
                        self.arg[4]=0
                self.ultra()
        def ultra(self)://Ultrasonic Sensor
                TRIG = 23
                ECHO = 24
                GPIO.setup(TRIG,GPIO.OUT)
                GPIO.setup(ECHO,GPIO.IN)
                GPIO.output(TRIG, False)
                time.sleep(0.1)
                GPIO.output(TRIG, True)
                time.sleep(0.00001)
                GPIO.output(TRIG, False) 
                while GPIO.input(ECHO)==0: 
                        pulse_start = time.time()
                while GPIO.input(ECHO)==1:
                        pulse_end = time.time()
                pulse_duration = pulse_end - pulse_start
                distance = pulse_duration * 17150
                self.arg[5] = round(distance, 2)
	def get(self):
		return self.arg


