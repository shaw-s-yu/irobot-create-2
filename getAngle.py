import create2api
import time
import json

bot=create2api.Create2()
bot.start()
bot.safe()
try:
    while True:
        bot.turn_counter_clockwise(20)
        time.sleep(0.5)
        bot.get_packet(100)
        print json.dumps(bot.sensor_state['angle'],indent=4,sort_keys=False)
        bot.stop()
except KeyboardInterrupt:
    bot.stop()
