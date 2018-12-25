import create2api
import time
from math import *
import json

bot=create2api.Create2()
bot.start()
bot.safe()

v=20
t1=6
t2=5

try:
    while True:
        bot.drive_straight(v)
        time.sleep(t2)
        bot.turn_clockwise(v)
        time.sleep(t1)
        print json.dumps(bot.sensor_state['angle'],indent=4,sort_keys=False)
except KeyboardInterrupt:
    bot.stop()

