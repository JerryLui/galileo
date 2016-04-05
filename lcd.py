import pyupm_i2clcd as upm_lcd
import pyupm_grove, time, mraa
from datetime import datetime
from pytz import timezone
import pytz

CET = timezone('CET')
lcd = upm_lcd.Jhd1313m1(0, 0x3E, 0x62)
temp = pyupm_grove.GroveTemp(2)
light = mraa.Aio(0)
var = 25
oldtime = 'holder'
lcd.setColor(var,0,0)

while 1:
    newtime = datetime.strftime(datetime.now(tz=CET), '%Y-%m-%d %H:%M')
    if oldtime != newtime: 
        lcd.clear()
        if light.read() < 480 and light.read() > 200:
            if var > 50:
                var -= 5
                lcd.setColor(var,0,0)
            elif var < 50:
                var += 5
                lcd.setColor(var,0,0)
        elif light.read() < 180:
            if var > 25:
                var -= 5
                lcd.setColor(var,0,0)
        else:
            if var < 125:
                var += 5
                lcd.setColor(var,0,0)
        lcd.setCursor(0,0)
        lcd.write(newtime)
        lcd.setCursor(1,0)
        lcd.write('Temperature: ' + str(temp.value()) + 'C')
        oldtime = newtime
    time.sleep(1)
