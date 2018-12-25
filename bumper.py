import create2api
import time
import json

def getSensor():
    bot.get_packet(100)
    global lb, rb, lc, lfc, rc, rfc
    lb=json.dumps(bot.sensor_state['wheel drop and bumps']['bump right'],indent=4,sort_keys=False)
    rb=json.dumps(bot.sensor_state['wheel drop and bumps']['bump left'],indent=4,sort_keys=False)
    lc=json.dumps(bot.sensor_state['cliff left'],indent=4,sort_keys=False)
    lfc=json.dumps(bot.sensor_state['cliff front left'],indent=4,sort_keys=False)
    rc=json.dumps(bot.sensor_state['cliff right'],indent=4,sort_keys=False)
    rfc=json.dumps(bot.sensor_state['cliff front right'],indent=4,sort_keys=False)

    lb=False if lb is 'false' else True
    rb=False if rb is 'false' else True
    lc=False if lc is 'false' else True
    rc=False if rc is 'false' else True
    lfc=False if lfc is 'false' else True
    rfc=False if rfc is 'false' else True

def bumpTurn():
    bot.drive_straight(-30)
    time.sleep(0.5)
    global lb, rb
    if lb:
        bot.turn_counter_clockwise(30)
        time.sleep(0.5)
        lb=False
        lrb=False
    elif rb:
        bot.turn_clockwise(30)
        time.sleep(0.5)
        lb=False
        rb=False

bot=create2api.Create2()
bot.start()
bot.safe()

lb=False
rb=False
lc=False
rc=False
lfc=False
rfc=False

try:
    while not lb and not rb and not lc and not lfc and not rc and not rfc:
        bot.drive_straight(30)
        getSensor()
        if lb or rb:
            bumpTurn()
except KeyboardInterrupt:
    bot.stop()
