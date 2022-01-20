led = 0
while led < 60: #scroll all rows at the same time
    for rows in range (6):
        if rows%2 == 1 :
           leds[59 - led + rows*60] = (255,255,255)
        elif rows%2 == 0 :
           leds[59 - led + rows*60] = (255,0,0)
        client.put_pixels(leds)
        time.sleep(0.1)
        led = led + 1
