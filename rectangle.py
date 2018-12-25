import create2api
from math import pi
import time

#create bot
bot = create2api.Create2()

#start
bot.start()
bot.safe()

#Enter info
turn=eval(input("Enter 1 for clockwise turn, else 2"))
v=eval(input("Enter velocity"))
length1=eval(input("Enter length of first side"))
length2=eval(input("Enter length of second side"))

#drive
for n in range(1,2):
    bot.drive_straight(v)
    time.sleep(length1/v)
    bot.drive_straight(0)
    bot.turn_clockwise(v) if turn is 1 else bot.turn_counter_clockwise(v)
    time.sleep((pi*235)/(4*v))
    bot.drive_straight(0)
    bot.drive_straight(v)
    time.sleep(length2/v)
    bot.drive_straight(0)
    bot.turn_clockwise(v) if turn is 1 else bot.turn_counter_clockwise(v)
    time.sleep((pi*235)/(4*v))
    bot.drive_straight(0)

#stop bot
bot.stop()
