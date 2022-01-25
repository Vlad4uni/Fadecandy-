import opc
import time

total_strips = 6
leds_per_strip = 60
address = 'localhost:7890'


def flag(client, total_strips=6, leds_per_strip=60):
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
    while True:
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


def main():
    client = opc.Client(address)
    print('Connected' if client.can_connect() else 'Not connected')
    flag(client, total_strips, leds_per_strip)


if __name__ == '__main__':
    main()
