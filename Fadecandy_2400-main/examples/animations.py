import opc
import time

total_strips = 6
leds_per_strip = 60
address = 'localhost:7890'


def question(client, total_strips=6, leds_per_strip=60):
    # the question mark art
    qmark = ''.join([
        s.center(leds_per_strip) for s in '''######
##  ##
    ##
  ##

  ##'''.split('\n')
    ])
    # set pixels based on character
    pixels = [(255, 0, 0) if c == '#' else (0, 0, 0) for c in qmark]
    # empty pixels
    empty = [(0, 0, 0) for _ in range(total_strips * leds_per_strip)]
    # run animation
    for _ in range(6):
        # question mark
        client.put_pixels(pixels, channel=0)
        time.sleep(0.5)
        # empty
        client.put_pixels(empty, channel=0)
        time.sleep(0.5)


def globe(client, total_strips=6, leds_per_strip=60):
    # the globe
    # '#' characters are colored in green. dots are blue. empty space is black.
    g = ''.join([
        s.center(leds_per_strip) for s in '''   .##.
   #....##.
  #....###..
  .#...##...
   ##....#.
   ##..'''.split('\n')
    ])

    # empty pixels
    empty = [(0, 0, 0) for _ in range(total_strips * leds_per_strip)]
    pixels = []
    for c in g:
        # add pixels depending on character
        if c == '#':
            pixels.append((0, 255, 0))
        elif c == '.':
            pixels.append((0, 0, 255))
        else:
            pixels.append((0, 0, 0))

    # run animation
    for _ in range(4):
        # colors
        client.put_pixels(pixels, channel=0)
        time.sleep(0.5)
        # empty
        client.put_pixels(empty, channel=0)
        time.sleep(0.5)


def american_flag(client, total_strips=6, leds_per_strip=60):
    # the flag
    f = [
        s.center(leds_per_strip) for s in '''******.....................
******---------------------
******.....................
---------------------------
...........................
---------------------------'''.split('\n')
    ]
    # the current round
    r = 0
    for i in range(120):
        pixels = []
        # increase round
        r += 1
        for line in f:
            for i, c in enumerate(line):
                # adjust color intensity each round
                i = (i - r) % 60
                # depending on the character set the color
                if c == '*':
                    p = (0, 0, 100 + i * 2)
                elif c == '.':
                    p = (100 + i * 2, 0, 0)
                elif c == '-':
                    p = (100 + i * 2, 100 + i * 2, 100 + i * 2)
                else:
                    p = (0, 0, 0)
                pixels.append(p)
        # set the leds and sleep for 0.02 seconds.
        client.put_pixels(pixels, channel=0)
        time.sleep(0.02)


def bulgarian_flag(client, total_strips=6, leds_per_strip=60):
    leds = [(192, 192, 192)] * 360  #silver
    client.put_pixels(leds)
    client.put_pixels(leds)
    led = 0
    while led < 60:  #scroll all rows at the same time
        for rows in range(2):  #first two rows left to right
            leds[led + rows * 60] = (255, 255, 255)
        for rows in range(2, 4):  #the next two row go inwards - right to left
            leds[59 - led + rows*60] = (34,139,34)
        for rows in range(4, 6):  #last two rows travel from the left to the right
            leds[led + rows * 60] = (255, 0, 0)
        client.put_pixels(leds)
        time.sleep(0.1)
        led = led + 1


def spanish_flag(client, total_strips=6, leds_per_strip=60):
    leds = [(192, 192, 192)] * 360  #silver
    client.put_pixels(leds)

    # light the first line in red
    for i in range(60):
        leds[i] = (255, 0, 0)
    client.put_pixels(leds)
    time.sleep(0.8)

    # light the second line in red
    for i in range(60, 120):
        leds[i] = (255, 0, 0)
    client.put_pixels(leds)
    time.sleep(0.8)

    # light the third line in yellow
    for i in range(120, 180):
        leds[i] = (255, 255, 0)
    client.put_pixels(leds)
    time.sleep(0.3)

    # light the fourth line in yellow
    for i in range(180, 240):
        leds[i] = (255, 255, 0)
    client.put_pixels(leds)
    time.sleep(0.8)

    # light the fifth line in red
    for i in range(240, 300):
        leds[i] = (255, 0, 0)
    client.put_pixels(leds)
    time.sleep(0.8)

    # light the sixth line in red
    for i in range(300, 360):
        leds[i] = (255, 0, 0)
    client.put_pixels(leds)
    time.sleep(0.8)



def flags(client):
    empty = [(0, 0, 0)] * 360
    american_flag(client)
    client.put_pixels(empty)
    time.sleep(1)
    bulgarian_flag(client)
    client.put_pixels(empty)
    time.sleep(1)
    spanish_flag(client)
    client.put_pixels(empty)
    time.sleep(1)

def end(client):
    # the colors of the end animation
    colors = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 255),
              (0, 255, 255), (255, 255, 0)]

    # the animation pattern
    # start with the cells numbered 1's and then go on till 4.
    pattern = [[
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 4, 0, 0, 3, 3, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    ],
               [
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 3, 0, 2, 2, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
               ],
               [
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 4, 3, 2, 1, 1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
               ],
               [
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 4, 3, 2, 1, 1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
               ],
               [
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 3, 0, 2, 2, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
               ],
               [
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 4, 0, 0, 3, 3, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
               ]]

    # flatten the grid into a 1d list
    pattern = [j for sub in pattern for j in sub]

    # run the animation
    for i in range(6):
        for i in range(1, 5):
            # if the color is more than the current cycle light it up.
            pixels = [colors[x] if i >= x else (0, 0, 0) for x in pattern]
            client.put_pixels(pixels, channel=0)
            time.sleep(0.3)


def clear(client):
    empty = [(0, 0, 0)] * 360
    client.put_pixels(empty, channel=0)
