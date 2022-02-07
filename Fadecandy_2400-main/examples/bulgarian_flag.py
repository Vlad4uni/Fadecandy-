import opc
import time
import random

leds = [(192,192,192)]*360 #silver

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

#Animation 2

led = 0
while led < 60:#scroll all rows at the same time
    for rows in range (2): #first three rows left to right
        leds[led + rows * 60] = (255,255,255)
    for rows in range (2,4): #first three rows left to right
        leds[59 - led + rows*60] = (34,139,34)
    for rows in range (4,6): #first three rows left to right
        leds[led + rows * 60] = (255,0,0)
    client.put_pixels(leds)
    time.sleep(0.1)
    led = led + 1
