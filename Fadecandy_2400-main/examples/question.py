import opc
import time

total_strips = 6
leds_per_strip = 60
address = 'localhost:7890'
client = opc.Client(address)



qmark = '\n'.join(
    [s.center(60) for s in '''######
    ##
    ##
  ##

  ##
'''.split('\n')])


def question(client, total_strips=6, leds_per_strip=60):
    qmark = ''.join([
        s.center(leds_per_strip) for s in '''######
##  ##
    ##
  ##

  ##'''.split('\n')
    ])
    pixels = [(255, 0, 0) if c == '#' else (0, 0, 0) for c in qmark]
    empty = [(0, 0, 0) for _ in range(total_strips * leds_per_strip)]
    while True:
        client.put_pixels(pixels, channel=0)
        time.sleep(0.5)
        client.put_pixels(empty, channel=0)
        time.sleep(0.5)


def main():
    question(client, total_strips, leds_per_strip)


if __name__ == '__main__':
    main()
