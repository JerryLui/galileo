#!/usr/bin/python

import mraa, time

# PIN ASSIGNMENTS
LED_PIN = 3
LIGHT_PIN = 0
BTN_PIN = 2

led = mraa.Pwm(LED_PIN)
light = mraa.Aio(LIGHT_PIN)
btn = mraa.Gpio(BTN_PIN)

btn.dir(mraa.DIR_IN)
led.enable(True)
led.period_ms(5)

UPPER_TH = 520
LOWER_TH = 160
intensity = 0

while 1:
    light_val = light.read()
    led_val = led.read()
    if light_val > UPPER_TH:
        intensity = 0
    elif light_val < LOWER_TH:
        if led_val < 0.99:
            if intensity >= 0.5:
                intensity += 0.1
            else:
                intensity += 0.05
    else:
        if led_val > 0.06:
            if intensity >= 0.5:
                intensity -= 0.1
            else:
                intensity -= 0.05
        elif led_val < 0.04:
            intensity += 0.05
    led.write(intensity)

    if btn.read() != 0:
        btn_pressed = True
        while btn_pressed:
            led.write(0)
            time.sleep(0.5)
            if btn.read() != 0:
                btn_pressed = False
                time.sleep(0.5)
    time.sleep(0.12)

