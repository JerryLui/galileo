import mraa
import pyupm_buzzer

buzz = mraa.Pwm(5)
buzz.enable(False)
