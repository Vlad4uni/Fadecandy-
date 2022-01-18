import opc
import time
import random

leds = [(192,192,192)]*360 #silver

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

#Animation 2

led = 0
while led < 60: #scroll all rows at the same time
    if row == 1:
       leds[led + row *60] = (0,0,255)
    client.put_pixels(leds)
    time.sleep(0.1)
    led = led + 1

