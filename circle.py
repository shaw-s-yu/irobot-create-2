import create2api
from math import *
import time
#Create bot and start
bot=create2api.Create2()
bot.start()
bot.safe()

#Enter r and v
radius=100
velocity=50

#Enter times
try:
    while True:
        bot.drive(velocity,radius)
except KeyboardInterrupt:
    bot.stop()



