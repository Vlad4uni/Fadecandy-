import opc
import time
import random

leds = [(255,255,255)]*360 #white

client = opc.Client('localhost:7890')
client.put_pixels(leds)
client.put_pixels(leds)

#Animation 1
#First roll goes from left to right
#Second roll goes from right to left
#Patter keeps repeating until it reaches the sixth strip

led = 0
while led < 60:#scroll all rows at the same time
    for rows in range (1): #first three rows left to right
        leds[led + rows * 60] = (220,20,60)
    for rows in range (1,2):#last three rows reversed (righty to left )
        leds[59 - led + rows*60] = (127,255,212)
    for rows in range (2,3): #first three rows left to right
        leds[led + rows * 60] = (220,20,60)
    for rows in range (3,4):#last three rows reversed (righty to left )
        leds[59 - led + rows*60] = (127,255,212)
    for rows in range (4,5): #first three rows left to right
        leds[led + rows * 60] = (220,20,60)
    for rows in range (5,6):#last three rows reversed (righty to left )
        leds[59 - led + rows*60] = (127,255,212)
    client.put_pixels(leds)
    time.sleep(0.1)
    led = led + 1

#Animation 2
