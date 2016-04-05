#!/usr/bin/python

import mraa, time, ephem

# Daytimechecker
CITY = 'Gothenburg'

sun = ephem.Sun()
city = ephem.city(CITY)
sun.compute(city)
twilight = -12 * ephem.degree

if sun.alt > twilight:
    btn_read = 1
else:
    btn_read = 0

# Pin assignments
LED_PIN = 3
TURN_PIN = 3
BTN_PIN = 2

led = mraa.Pwm(LED_PIN)
turn = mraa.Aio(TURN_PIN)
btn = mraa.Gpio(BTN_PIN)

btn.dir(mraa.DIR_IN)
led.enable(True)
led.period_ms(5)

counter = 0
epsilon = 2
intensity = 0.05

while 1: 
    if btn_read != 0:
        led.write(0)
        btn_pressed = True
        time.sleep(0.24)
        while btn_pressed:
            if btn.read() != 0:
                btn_pressed = False
                led.write(intensity)
                time.sleep(0.24)
            time.sleep(0.24)

    turn_val = turn.read()
    if counter < 10:
        intensity = round(turn_val**2/1046529.0, 2)
        led.write(intensity)
        counter += 1
        ol_turn_val = turn_val
    elif turn_val > ol_turn_val + epsilon or turn_val < ol_turn_val - epsilon:
        counter = 0
    
    time.sleep(0.12)
    btn_read = btn.read()

