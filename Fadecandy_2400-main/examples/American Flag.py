import opc
import time
import random

leds = [(192,192,192)]*360 #silver

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

#Animation 2

led = 0
led [244] = (255,0,0)
#while led < 60:#scroll all rows at the same time
#    for rows in range (1): #first row red 
#        leds[led + rows * 60] = (255,0,0)
#    for rows in range (1,2):#last three rows reversed (righty to left )
#        leds[59 - led + rows*60] = (255,255,255)
#    for rows in range (2,3): #first three rows left to right
#        leds[led + rows * 60] = (255,0,0)
#    for rows in range (3,4):#last three rows reversed (righty to left )
#        leds[59 - led + rows*60] = (255,255,255)
#    for rows in range (4,5): #first three rows left to right
#        leds[led + rows * 60] =  (255,0,0)
#    for rows in range (5,6):#last three rows reversed (righty to left )
#        leds[59 - led + rows*60] = (255,255,255)
#    client.put_pixels(leds)
#    time.sleep(0.1)
#    led = led + 1

