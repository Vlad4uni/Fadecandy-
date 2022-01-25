import opc
import time

total_strips = 6
leds_per_strip = 60
address = 'localhost:7890'


def globe(client, total_strips=6, leds_per_strip=60):
    # the globe
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
    while True:
        # colors
        client.put_pixels(pixels, channel=0)
        time.sleep(0.5)
        # empty
        client.put_pixels(empty, channel=0)
        time.sleep(0.5)


def main():
    client = opc.Client(address)
    print('Connected' if client.can_connect() else 'Not connected')
    globe(client, total_strips, leds_per_strip)


if __name__ == '__main__':
    main()
