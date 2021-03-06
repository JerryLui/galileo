import mraa
import time

PWM_PIN = 3
ADC_PIN = 0	# Analog in pin
LIGHT_MAX = 1023.0

pwm = mraa.Pwm(PWM_PIN)
pwm.enable(True)
pwm.period_us(5000)

adc = mraa.Aio(ADC_PIN)

while 1:
	light = adc.read()
	if light > 300:		# Threshold light intensity
		pwm.write(0)
		time.sleep(1)
	else:
		light_intensity = 1-light/LIGHT_MAX
		pwm.write(light_intensity)
		time.sleep(1)
	




	
 