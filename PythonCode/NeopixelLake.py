import time
import board
import neopixel

pixels= neopixel.NeoPixel(board.D5, 10)


#pixels.fill((0,0,255))
#pixels.brightness= 0.2

while True:
    pixels.fill((40, 200, 255))
    time.sleep(1)

    pixels.fill((20, 150, 230))
    time.sleep(1.2)

    pixels.fill((10, 70, 200))
    time.sleep(1)

    pixels.fill((3, 10, 150))
    time.sleep(1.2)

    pixels.fill((2, 6, 100))
    time.sleep(1)

    pixels.fill((1, 3, 50))
    time.sleep(1)
