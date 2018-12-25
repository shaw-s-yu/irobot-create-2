import create2api
import time
import json

bot=create2api.Create2()
bot.start()
bot.safe()

v=20
bot.turn_clockwise(v)
time.sleep(0.5)
bot.get_packet(v)
vl=json.dumps(bot.sensor_state['requested left velocity'],indent=4,sort_keys=False)
vr=json.dumps(bot.sensor_state['requested right velocity'],indent=4,sort_keys=False)
angle=json.dumps(bot.sensor_state['angle'],indent=4,sort_keys=False)
#angle=int(angle,16)
vl=int(vl,16)
vr=int(vr,16)
print 'vl:',vl
print 'vr:',vr
print 'angle:',angle
bot.stop()
