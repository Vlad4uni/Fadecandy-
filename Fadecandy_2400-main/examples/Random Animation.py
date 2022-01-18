import opc
import time

total_strips = 6
leds_per_strip = 60
client =opc.Client('localhost:7890')

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 255), (0, 255, 255),
          (255, 255, 0)]


while True:
    strips = []
    for i in range(total_strips):
        strips = [[(0, 0, 0) for led in range(leds_per_strip)]
                  for strip in range(total_strips)]
        strips[i] = [colors[i] for pixel in range(leds_per_strip)]
        pixels = [j for sub in strips for j in sub]
        client.put_pixels(pixels, channel=0)
        time.sleep(0.3)
