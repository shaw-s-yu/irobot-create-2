import create2api
from math import *
from time import *
#create bot
bot = create2api.Create2()

#start
bot.start()
bot.safe()

#Enter info
a=eval(input("Enter the length of first line(mm)"))
b=eval(input("Enter the degree of first angle turn"))
c=eval(input("Enter the degree of second angle turn"))
d=eval(input("Enter 1 for clockwise turn, else 2"))
v=input("Enter velocity")

#drive
bot.drive_straight(v)
sleep(a/v)     #1st side
bot.drive_straight(0)
bot.turn_clockwise(v) if d is 1 else bot.turn_counter_clockwise(v)
sleep(b*235*pi)/(360*double(v)))  #1st angle
bot.drive_straight(0)
bot.drive_straight(v)
sleep((a*sin(180-b-c))/(sin(c)*double(v))) #2nd side
bot.drive_straight(0)
bot.turn_clockwise(v) if d is 1 else bot.turn_counter_clockwise(v)
sleep((235*pi*c)/(360*double(v)))  #2nd angle
bot.drive_straight(0)
bot.drive_straight(v)
sleep((a*sin(b))/(sin(c)*double(v)))   #3rd side
bot.drive_straight(0)
bot.turn_clockwise(v) if d is 1 else bot.turn_counter_clockwise(v)
sleep(((180-b-c)*235*pi)/(360*double(v)))    #3rd angle
bot.drive_straight(0)

#stop bot
bot.stop()

    


