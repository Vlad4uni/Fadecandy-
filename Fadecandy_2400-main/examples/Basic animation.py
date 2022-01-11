import opc
import time
import random

leds = [(255,255,255)]*360 #white

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

#for led in leds: #pick out an element:led (255,255,255)
for led in range(len(leds)):
    leds [led] = (255,0,0)
    time.sleep(.1)
    client.put_pixels(leds)
