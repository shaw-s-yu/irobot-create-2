import create2api
from math import pi
import time

bot = create2api.Create2()
bot.start()
bot.safe()

try:
    while True:
        bot.drive_straight(50)
        time.sleep(5)
        bot.turn_clockwise(50)
        time.sleep(pi*235/(4*50))
except KeyboardInterrupt:
    bot.stop()
